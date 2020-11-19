from src.main.user_registration.validation import Validation
import re


class Name(Validation):
    def validate_input(self, user_input):
        name_regex = "^[A-Z][a-z]{2,} [A-Z][a-z]{2,}$"
        match_pattern = re.match(name_regex, user_input)
        return False if match_pattern == None else True
