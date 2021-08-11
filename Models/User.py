

class User:

    """
    User class to represent a user.
    ...

    Attributes
    ----------
    id : int
        Unique id of the user.
    fullname : str
        fullname of the user.
    email : str
        email of the user.
    phone : str
        phone of the user.

    Methods
    -------
    getData(db_name: str = "users.txt")
        Returns a list of all users.

    """

    def __init__(self, id: int, fullname: str, email: str, phone: str):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.phone = phone
