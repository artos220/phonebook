import notifier
import messages as constants


def input_value(message):
    while True:
        value = input(message).strip().upper()
        if value:
            return value
        notifier.notify('input_some_data')


def input_cmd():
    return input_value(constants.MSG_INPUT_CMD)


def input_name():
    return input_value(constants.MSG_INPUT_NAME)


def input_phone():
    while True:
        phone = input_value(constants.MSG_INPUT_PHONE)
        if phone.isdigit():
            return phone
        notifier.notify('value_not_digit', phone)


def input_email():
    return input_value(constants.MSG_INPUT_EMAIL)
