from view import argparse_


class CmdView:
    def __init__(self, obj):
        key = obj.get_input_type('key')
        self.value = str(argparse_.args.parse_args().__dict__[key.lower()]).upper()

    def __repr__(self):
        return f'{self.value}'
