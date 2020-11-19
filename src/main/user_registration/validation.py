from abc import ABC, abstractmethod


class Validation(ABC):
    @abstractmethod
    def validate_input(self, user_input):
        pass
