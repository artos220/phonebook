# Author: Artem Osmina
# Description: Simple Phone Book

from controller import controller
from view import notifier, inputs
from configs import config_reader as config, cmd_argpars


def not_found_cmd(cmd_):
    return lambda: notifier.notify('not_found_cmd', cmd_)


# TODO need view class for menu and cmd
menu_action = {'C': controller.contact_create,
               'R': controller.contact_read,
               'U': controller.contact_update,
               'D': controller.contact_delete,
               'A': controller.phonebook_read,
               'S': controller.phonebook_save,
               'H': controller.help_,
               'Q': controller.quit_,
               }

args = cmd_argpars.args.parse_args()

try:
    notifier.notify('hello')
    controller.phonebook_load()
    if config.INPUT_TYPE.lower() == 'cmd':
        cmd = args.cmd.upper()
        menu_action.get(cmd, not_found_cmd(cmd))()
    else:
        while True:
            cmd = inputs.input_cmd()
            menu_action.get(cmd, not_found_cmd(cmd))()
finally:
    controller.phonebook_save()
    notifier.notify('exit')

