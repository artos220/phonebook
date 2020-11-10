import notifier
import messages as constants


def input_cmd():
    while True:
        cmd = input(constants.MSG_INPUT_CMD).strip().upper()
        if cmd:
            return cmd
        notifier.notify('input_some_data')


def input_name():
    while True:
        name = input(constants.MSG_INPUT_NAME).strip().upper()
        if name:
            return name
        notifier.notify('input_some_data')


def input_phone():
    while True:
        phone = input(constants.MSG_INPUT_PHONE).strip().upper()
        if phone:
            if phone.isdigit():
                return phone
            notifier.notify('value_not_digit', phone)
        notifier.notify('input_some_data')
