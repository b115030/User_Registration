from src.main.user_registration.validation import Validation
import re


class Email(Validation):
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
        email_regex = "^[a-zA-Z0-9]+[\\.\\-\\+\\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]?[a-zA-Z]{2,4}[\\.]?([a-z]{2,4})?$"
        match_pattern = re.match(email_regex, user_input)
        return False if match_pattern == None else True
