# Author: Artem Osmina
# Description: Simple Phone Book

from controller import controller
from view import notifier, view
from configs import config_reader as config
from configs import messages as constants
from view.view import View


def not_found_cmd(cmd_):
    return lambda: notifier.notify('not_found_cmd', cmd_)


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
    notifier.notify('hello')
    controller.phonebook_load()
    if config.INPUT_TYPE.lower() == 'cmd':
        cmd = View('cmd').value
        menu_action.get(cmd, not_found_cmd(cmd))()
    else:
        while True:
            cmd = View(constants.MSG_INPUT_CMD).value
            menu_action.get(cmd, not_found_cmd(cmd))()
finally:
    controller.phonebook_save()
    notifier.notify('exit')

