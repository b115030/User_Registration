from src.main.user_registration.validation import Validation
import re


class Phone(Validation):

    def validate_input(self, input_data):
        phone_regex = "^[0-9]{2} [0-9]{10}$"
        match_pattern = re.match(phone_regex, input_data)
        return False if match_pattern == None else True
