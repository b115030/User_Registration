from src.main.user_registration.user_registration import User_Validation
def test_print_message():
    user_validation = User_Validation()
    assert user_validation.print_message()
