from src.main.user_registration.name import Name
from src.main.user_registration.email import Email
from src.main.user_registration.phone import Phone
from src.main.user_registration.password import Password


class RegistrationFactory:
    def return_object(self, input_type):
        switcher = {
            "name": Name(),
            "email": Email(),
            "phone": Phone(),
            "password": Password()
        }
        return switcher.get(input_type)
