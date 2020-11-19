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
        result = user_registration.get_input(user_input_type, user_input_data)
        assert result == expected

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
        result = user_registration.get_input(user_input_type, user_input_data)
        assert result == expected

    @pytest.mark.parametrize("user_input_type, user_input_data, expected", [
        ("phone", "91 9876541123", True),
        ("phone", "911 987456321", False),
        ("phone", "919438268759", False),
        ("phone", "91 98745632", False),
        ("phone", "91 9432658745692", False)
    ])
    def test_given_phone_no_when_valid_or_invalid_returns_result(self, user_input_type, user_input_data, expected):
        user_registration = UserRegistration()
        result = user_registration.get_input(user_input_type, user_input_data)
        assert result == expected

    @pytest.mark.parametrize("user_input_type, user_input_data, expected", [
        ("password", "Abcdefghi", False),
        ("password", "12345678", False),
        ("password", "Abcdefghi", False),
        ("password", "Abcde123", False),
        ("password", "Ab@12", False),
        ("password", "Abcde@123", True),
        ("password", "Abcde@@12", False)
    ])
    def test_given_password_when_valid_or_invalid_returns_result(self, user_input_type, user_input_data, expected):
        user_registration = UserRegistration()
        result = user_registration.get_input(user_input_type, user_input_data)
        assert result == expected
