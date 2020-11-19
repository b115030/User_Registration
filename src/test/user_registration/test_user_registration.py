from src.main.user_registration.user_registration import UserRegistration
import pytest


class TestUserRegistration:

    @pytest.mark.parametrize("user_input_type, user_input_data, expected", [
        ("name", "Gopinath Das", True),
        ("name", "gopinath Das", False),
        ("name", "Gopinath das", False),
        ("name", "GopinathDas", False),
        ("name", "G Das", False),
        ("name", "Gopinath D", False)
    ])
    def test_given_first_name_when_valid_should_return_true(self, user_input_type, user_input_data, expected):
        user_registration = UserRegistration()
        is_valid = user_registration.get_input(user_input_type, user_input_data)
        assert is_valid == expected

    @pytest.mark.parametrize("user_input_type, user_input_data, expected", [
        ("email", "abc@yahoo.com", True),
        ("email", "abc-100@yahoo.com", True),
        ("email", "abc.100@yahoo.com", True),
        ("email", "abc111@abc.com", True),
        ("email", "abc-100@abc.net", True),
        ("email", "abc.100@abc.com.au", True),
        ("email", "abc@1.com", True),
        ("email", "abc@gmail.com.com", True),
        ("email", "abc+100@gmail.com", True),
        ("email", "abc", False),
        ("email", "abc@.com.my", False),
        ("email", "abc123@gmail.a", False),
        ("email", "abc123@.com", False),
        ("email", "abc123@.com.com", False),
        ("email", ".abc@abc.com", False),
        ("email", "abc()*@gmail.com", False),
        ("email", "abc@%*.com", False),
        ("email", "abc..2002@gmail.com", False),
        ("email", "abc.@gmail.com", False),
        ("email", "abc@abc@gmail.com", False),
        ("email", "abc@gmail.com.1a", False),
        ("email", "abc@gmail.com.aa.au", False)
    ])
    def test_given_email_when_valid_or_invalid_returns_result(self, user_input_type, user_input_data, expected):
        user_registration = UserRegistration()
        is_valid = user_registration.get_input(user_input_type, user_input_data)
        assert is_valid == expected
