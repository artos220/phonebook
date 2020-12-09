# Author: Artem Osmina
# Description: Simple Phone Book with mvc paradigm

from controller import controller
from view.notifier import notify
from view.view import View
from configs import config_reader as config, messages as constants


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


menu_action = {'C': controller.contact_create,
               'R': controller.contact_read,
               'U': controller.contact_update,
               'D': controller.contact_delete,
               'A': controller.phonebook_read,
               'S': controller.phonebook_save,
               'H': controller.help_,
               'Q': controller.quit_,
               }

try:
    notify('hello')
    controller.phonebook_load()
    while True:
        cmd = View(Cmd()).value
        menu_action.get(cmd, not_found_cmd(cmd))()
        if config.INPUT_TYPE.lower() == 'cmd':
            break

finally:
    controller.phonebook_save()
    notify('exit')
