from src.main.user_registration.validation import Validation
import re

class Password(Validation):
    def validate_input(self, user_input):
        password_regex = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        match_pattern = re.match(password_regex, user_input)
        return False if match_pattern == None else True