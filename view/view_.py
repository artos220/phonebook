from configs import cmd_argpars
from view import input_


class InputView:
    def __init__(self, msg_input, *args, **kwargs):
        self.value = input_.get_input(msg_input)

    def __repr__(self):
        return f'{self.value}'


class CmdView:
    def __init__(self, key, *args, **kwargs):
        self.value = str(cmd_argpars.args.parse_args().__dict__[key.lower()]).upper()

    def __repr__(self):
        return f'{self.value}'
