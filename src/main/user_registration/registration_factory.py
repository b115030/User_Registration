from src.main.user_registration.name import Name
from src.main.user_registration.email import Email
from src.main.user_registration.phone import Phone


class RegistrationFactory:
    def return_object(self, input_type):
        switcher = {
            "name": Name(),
            "email": Email(),
            "phone": Phone()
        }
        return switcher.get(input_type)
