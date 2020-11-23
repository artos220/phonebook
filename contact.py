import messages as constants


def input_value(message):
    while True:
        value = input(message).strip().upper()
        if value:
            return value


class Name:
    def __init__(self):
        self.value = input_value(constants.MSG_INPUT_NAME)

    def __repr__(self):
        return self.value


class Phone:
    def __init__(self):
        while True:
            phone = input_value(constants.MSG_INPUT_PHONE)
            if phone.isdigit():
                self.value: int = int(phone)
                break

    def __repr__(self):
        return self.value


class Email:
    def __init__(self):
        self.value = input_value(constants.MSG_INPUT_EMAIL)

    def __repr__(self):
        return self.value


class Contact:
    def __init__(self, name='', phone='', email=''):
        """ self.contacts list has all attr except name """
        self.name = name if name else Name().value
        self.phone = phone if phone else Phone().value
        self.email = email if email else Email().value
        self.contacts: [] = [value for attr, value in self.__dict__.items() if attr != 'name']

    def __repr__(self):
        """ return name=JHON, phone=123456, ... attr=value """
        repr_ = ''
        for attr, value in self.__dict__.items():
            repr_ = f'{repr_}{attr}={value}, '
        return f'{repr_[:-2]}'
