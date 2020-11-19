from src.main.user_registration.name import Name
from src.main.user_registration.email import Email


class RegistrationFactory:
    def return_object(self, input_type):
        switcher = {
            "name": Name(),
            "email": Email()
        }
        return switcher.get(input_type)
