from src.main.user_registration.validation import Validation
from src.main.user_registration.user_registration_exception import UserRegistrationException

import re


class Name(Validation):
    '''

    validates email using regex

    Methods:
        validate_input: matches user_input to email regex
    '''

    def validate_input(self, user_input):
        '''

        :param user_input: the user input to validate
        :type user_input: str
        :return: False if match_pattern == None else True
        :rtype: bool
        '''
        name_regex = "^[A-Z][a-z]{2,} [A-Z][a-z]{2,}$"
        match_pattern = re.match(name_regex, user_input)
        # if not match_pattern:
        #     raise UserRegistrationException("Enter the name with atleast 3 letters in first name and last name and a space in between")
        return False if match_pattern == None else True
