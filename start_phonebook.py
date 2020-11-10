# Author: Artem Osmina
# Description: Simple Phone Book
# add package dumper for load/save phonebook

import controler
import notifier
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
    notifier.notify('hello')
    controler.phonebook_load()
    while True:
        cmd = inputs.input_cmd()
        menu_action.get(cmd, lambda: notifier.notify('not_found_cmd', cmd))()
finally:
    controler.phonebook_save()
    notifier.notify('exit')
