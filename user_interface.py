from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_information(self, information):
        pass

    @abstractmethod
    def get_user_input(self, prompt):
        pass
