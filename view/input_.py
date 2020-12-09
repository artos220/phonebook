def get_input(message):
    while True:
        value = input(message).strip().upper()
        return value
        # notifier.notify('input_some_data')


class InputView:
    def __init__(self, obj):
        msg_input = obj.get_input_type('msg_input')
        self.value = get_input(msg_input)

    def __repr__(self):
        return f'{self.value}'
