def get_input(message):
    while True:
        value = input(message).strip().upper()
        if value:
            return value
        # notifier.notify('input_some_data')


class InputView:
    def __init__(self, msg_input, *args, **kwargs):
        self.value = get_input(msg_input)

    def __repr__(self):
        return f'{self.value}'
