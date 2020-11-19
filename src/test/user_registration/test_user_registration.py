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
