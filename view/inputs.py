from view import notifier
from configs import messages as constants


# TODO need view class for menu and cmd
def input_value(message):
    while True:
        value = input(message).strip().upper()
        if value:
            return value
        notifier.notify('input_some_data')


def input_cmd():
    return input_value(constants.MSG_INPUT_CMD)
