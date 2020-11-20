from src.main.user_registration.validation import Validation
import re


class Phone(Validation):
    '''

    validates phone number using regex

    Methods:
            validate_input: matches user_input to phone number regex
    '''

    def validate_input(self, input_data):
        '''

        :param user_input: the user input to validate
        :type user_input: str
        :return: False if match_pattern == None else True
        :rtype: bool
        '''
        phone_regex = "^[0-9]{2} [0-9]{10}$"
        match_pattern = re.match(phone_regex, input_data)
        return False if match_pattern == None else True
