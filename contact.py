import messages as constants


def input_value(message):
    while True:
        value = input(message).strip().upper()
        if value:
            return value


class Attribute:
    def __init__(self, value):
        self.name = self.name
        self.msg_input = self.msg_input
        if value:
            self.value = value
        else:
            self.value = self._validate(input_value(self.msg_input))

    def _validate(self, value):
        return value

    def __repr__(self):
        return f'{self.value}'


class Name(Attribute):
    name = 'Name'
    msg_input = constants.MSG_INPUT_NAME


class Phone(Attribute):
    name = 'Phone'
    msg_input = constants.MSG_INPUT_PHONE

    def _validate(self, value):
        if value.isdigit():
            return int(value)
        raise ValueError


class Email(Attribute):
    name = 'Email'
    msg_input = constants.MSG_INPUT_EMAIL


class Contact:
    def __init__(self, name, phone, email):
        """ self.contacts list has all attr except name """
        self.name = Name(name).value
        self.phone = Phone(phone).value
        self.email = Email(email).value
        self.contacts = [value for attr, value in self.__dict__.items() if attr != 'name']

    def set_name(self, name):
        self.name = Name(name).value

    def set_phone(self, phone):
        self.phone = Phone(phone).value

    def set_email(self, email):
        self.email = Email(email).value

    def __repr__(self):
        """ return name=JHON, phone=123456, ... attr=value """
        repr_str = ''
        for attr, value in self.__dict__.items():
            repr_str = f'{repr_str}{attr}={value}, '
        return f'{repr_str[:-2]}'
