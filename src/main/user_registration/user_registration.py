from src.main.user_registration.registration_factory import RegistrationFactory


class UserRegistration:
    def get_input(self, input_type, input_data):
        factory = RegistrationFactory()
        validate = factory.return_object(input_type)
        return validate.validate_input(input_data)
