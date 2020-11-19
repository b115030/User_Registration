from src.main.user_registration.validation import Validation
import re


class Email(Validation):
    def validate_input(self, user_input):
        email_regex = "^[a-zA-Z0-9]+[\\.\\-\\+\\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]?[a-zA-Z]{2,4}[\\.]?([a-z]{2,4})?$"
        match_pattern = re.match(email_regex, user_input)
        return False if match_pattern == None else True
