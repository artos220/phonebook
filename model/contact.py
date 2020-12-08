from configs import messages as constants
from view.view import View


class Attribute:
    def __init__(self):
        self.value = self._validate(View(self.key, self.msg_input).value)  # TODO maybe need to place args into view ?

    def _validate(self, value):
        if value:
            return value

    def __repr__(self):
        return f'{self.value}'


class Name(Attribute):
    key = 'Name'
    msg_input = constants.MSG_INPUT_NAME


class Phone(Attribute):
    key = 'Phone'
    msg_input = constants.MSG_INPUT_PHONE

    def _validate(self, value):
        if value:
            if str(value).isdigit():
                return int(value)
            raise ValueError


class Email(Attribute):
    key = 'Email'
    msg_input = constants.MSG_INPUT_EMAIL


class NullObject:
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
            return NullObject()


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
        return repr(self.contacts)
