from configs import messages as constants
from view.view import View


class Attribute:
    def __init__(self):
        self.value = self._validate(View(self).value)

    def _validate(self, value):
        return value

    def get_input_type(self, name):
        if name == 'msg_input':
            return self.msg_input
        else:
            return self.key

    def __repr__(self):
        return f'{self.value}'


class Name(Attribute):
    key = 'Name'
    msg_input = constants.MSG_INPUT_NAME


class Phone(Attribute):
    key = 'Phone'
    msg_input = constants.MSG_INPUT_PHONE

    def _validate(self, value):
        if str(value).isdigit():
            return int(value)
        raise ValueError


class Email(Attribute):
    key = 'Email'
    msg_input = constants.MSG_INPUT_EMAIL


class NullObject:
    key = ''
    value = ''

    def __getattr__(self, item):
        return lambda *args, **kwargs: None


class AttributesFab:
    def __new__(cls, key):
        if key == 'Name':
            return Name().value
        elif key == 'Phone':
            return Phone().value
        elif key == 'Email':
            return Email().value
        else:
            return NullObject().value


class Contact:
    def __init__(self):
        self.name = Name().value
        self.attr = []
        self.contacts = {}
        self.set_attr(self.attr)

    def set_attr(self, attr=('Phone', 'Email')):
        self.attr = list(attr)
        self.contacts = {key: AttributesFab(key) for key in attr}

    def __repr__(self):
        return f'{self.contacts}'
