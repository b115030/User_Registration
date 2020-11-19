from src.main.user_registration.name import Name


class RegistrationFactory:
    def return_object(self, input_type):
        switcher = {
            "name": Name()
        }
        return switcher.get(input_type)
