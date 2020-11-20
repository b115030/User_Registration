from src.main.user_registration.validation import Validation
import re


class Password(Validation):
    '''

    validates password using regex

    Methods:
        validate_input: matches user_input to password regex
    '''
    def validate_input(self, user_input):
        '''

        :param user_input: the user input to validate
        :type user_input: str
        :return: False if match_pattern == None else True
        :rtype: bool
        '''
        password_regex = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        match_pattern = re.match(password_regex, user_input)
        return False if match_pattern == None else True
