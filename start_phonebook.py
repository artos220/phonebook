# Author: Artem Osmina
# Description: Simple Phone Book
# config and save/load contacts file

import controler
import notifications
import inputs

menu_action = {'C': controler.contact_create,
               'R': controler.contact_read,
               'U': controler.contact_update,
               'D': controler.contact_delete,
               'A': controler.phonebook_read,
               'S': controler.phonebook_save,
               'H': controler.help_,
               'Q': controler.quit_,
               }

try:
    notifications.notify('hello')
    controler.phonebook_load()
    while True:
        cmd = inputs.input_cmd()
        menu_action.get(cmd, lambda: notifications.notify('not_found_cmd', cmd))()
finally:
    controler.phonebook_save()
    notifications.notify('exit')
