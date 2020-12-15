# Author: Artem Osmina
# Description: Simple Phone Book with mvc paradigm

from controller import controller
from view.view import View
from view.io_ import IO
from configs import config_reader as config
from view.cmd_ import Cmd, not_found_cmd

log_ = IO.log_
log_('start')
controller.phonebook_load()


menu_action = {'C': controller.contact_create,
               'R': controller.contact_read,
               'U': controller.contact_update,
               'D': controller.contact_delete,
               'A': controller.phonebook_read,
               'S': controller.phonebook_save,
               'H': controller.help_,
               'Q': controller.quit_,
               }


def start():
    while True:
        cmd = View(Cmd()).value
        menu_action.get(cmd, not_found_cmd(cmd))()
        if config.INPUT_TYPE.lower() == 'cmd':
            break


def finish():
    if config.INPUT_MODE.lower() == 'telnet':
        IO.telnet_server_shutdown()

    controller.phonebook_save()


if __name__ == "__main__":
    try:
        start()
    finally:
        finish()
