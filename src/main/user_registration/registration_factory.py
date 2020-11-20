from src.main.user_registration.name import Name
from src.main.user_registration.email import Email
from src.main.user_registration.phone import Phone
from src.main.user_registration.password import Password


class RegistrationFactory:
    '''

    This class takes in the object type and returns the object of respective type
    Methods:
        return_object
    '''

    def return_object(self, input_type):
        '''

        :param input_type: type of user detail
        :type input_type: str
        :return: object of respective classes
        :rtype: object
        '''
        switcher = {
            "name": Name(),
            "email": Email(),
            "phone": Phone(),
            "password": Password()
        }
        return switcher.get(input_type)
