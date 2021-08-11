from abc import ABC, abstractmethod


class BaseController(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def delete_by_id(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def write_data(self):
        pass
