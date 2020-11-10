# Author: Artem Osmina
# Description: Simple Phone Book
# add package dumper for load/save phonebook

import controller
import notifier
import inputs

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
    while True:
        cmd = inputs.input_cmd()
        menu_action.get(cmd, lambda: notifier.notify('not_found_cmd', cmd))()
finally:
    controller.phonebook_save()
    notifier.notify('exit')
