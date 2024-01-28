from user_interface import UserInterface

class ConsoleInterface(UserInterface):
    def display_information(self, information):
        print(information)

    def get_user_input(self, prompt):
        return input(prompt)
