from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersOnlyValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class LengthPassValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your passcode must be exactly 6 digits!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if len(value) != 6 or not value.isdigit():
            raise ValidationError(self.message)
