from src.main.user_registration.registration_factory import RegistrationFactory
from src.main.user_registration.user_registration_exception import UserRegistrationException


class UserRegistration:
    def get_input(self, input_type, input_data):
        '''

        :param input_type: user input type
        :param input_data: the user detail
        :return: validate_input(input_data)
        '''
        if not input_data:
            raise UserRegistrationException("input data cannot be empty")
        if not input_type:
            raise UserRegistrationException("input type cannot be empty")
        factory = RegistrationFactory()
        validate = factory.return_object(input_type)
        return validate.validate_input(input_data)
