import pytest
from src.main.user_registration.user_registration import UserRegistration


@pytest.fixture()
def user_registration_object():
    user_registration = UserRegistration()
    return user_registration
