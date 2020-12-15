from view import argparse_
from configs import messages as constants
from view.notifier import notify
from view.io_ import IO

data_input_ = IO.data_input_


class CmdView:
    def __init__(self, obj):
        key = obj.get_input_type('key')
        s = data_input_('').strip().lower()
        args = [s]  # ['-cmd=r', '-name=bob']
        self.value = str(argparse_.args.parse_args(args).__dict__[key.lower()]).upper()

    def __repr__(self):
        return f'{self.value}'


class Cmd:
    key = 'Cmd'
    msg_input = constants.MSG_INPUT_CMD

    def get_input_type(self, name):
        if name == 'msg_input':
            return self.msg_input
        else:
            return self.key


def not_found_cmd(cmd_):
    return lambda: notify('not_found_cmd', cmd_)
