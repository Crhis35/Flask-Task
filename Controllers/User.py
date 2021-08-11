import csv
from typing import Type  # you have to import Type

from Models.User import User
from Controllers.Base import BaseController


class UserController(BaseController):
    _instance = None
    users = []

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def reset(self) -> 'UserController':
        self.users = []
        return self._instance

    @classmethod
    def getInstance(self) -> 'UserController':
        if self._instance is None:
            self._instance = self.__new__(self)
        return self._instance

    @classmethod
    def get_all(self, db_name: str = "users.csv") -> list:
        """
        Get all users from the database.


        If the argument `db_name` isn't passed in, the default fine "users.csv" will be used.

        Parameters
        ----------
        db_name : str, optional
            The file name to load (default is users.csv).

        Raises
        ------
        NotImplementedError
            Not file found.
        """
        self.reset()
        db_pos = './db/'+db_name

        with open(db_pos, 'a+') as f:
            pass

        with open(db_pos) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                self.users.append(User(row[0], row[1], row[2], row[3]))

        return self.users

    @classmethod
    def get_by_id(self, id: int) -> 'User':
        """
        Get a user by id.

        Parameters
        ----------
        id : int
            The id of the user to get.

        Raises
        ------
        ValueError
            User not found.
        """
        self.get_all()

        for user in self.users:
            if user.id == id:
                return user
        raise ValueError("User not found.")

    @classmethod
    def delete_by_id(self, id: int) -> None:
        """
        Delete a user by id.

        Parameters
        ----------
        id : int
            The id of the user to delete.

        Raises
        ------
        ValueError
            User not found.
        """
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                self.write_data()
                return
        raise ValueError("User not found.")

    @classmethod
    def add(self, user: 'User') -> None:
        """
        Add a user to the database.

        Parameters
        ----------
        user : User
            The user to add.

        Raises
        ------
        ValueError
            User already exists.
        """

        if user in self.users:
            raise ValueError("User already exists.")
        self.users.append(user)
        self.write_data()

    @classmethod
    def write_data(self, db_name: str = "users.csv") -> None:
        """
        Write all users to the database.

        Parameters
        ----------
        db_name : str, optional
            The file name to write (default is users.csv).

        Raises
        ------
        NotImplementedError
            Not file found.
        """
        db_pos = './db/'+db_name

        with open(db_pos, 'w+') as f:
            pass

        with open(db_pos, 'a+') as f:
            csv_writer = csv.writer(f, delimiter=',')
            for user in self.users:
                csv_writer.writerow(
                    [user.id, user.fullname, user.email, user.phone])

    @classmethod
    def update(self, id: int, fullname: str, email: str, phone: str) -> None:
        """
        Update a user.

        Parameters
        ----------
        user : User
            The user to update.

        Raises
        ------
        ValueError
            User not found.
        """
        self.get_all()

        for user in self.users:
            if user.id == id:
                user.fullname = fullname
                user.email = email
                user.phone = phone
                self.write_data()
                return
        raise ValueError("User not found.")

    @classmethod
    def delete(self, id: int) -> None:
        """
        Delete a user.

        Parameters
        ----------
        id : int
            The id of the user to delete.

        Raises
        ------
        ValueError
            User not found.
        """
        self.get_all()

        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                self.write_data()
                return
        raise ValueError("User not found.")
