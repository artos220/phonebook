# Author: Artem Osmina
# Description: Simple Phone Book

import controller
import notifier
import inputs
import cmd_argpars


def not_found_cmd(cmd_):
    return lambda: notifier.notify('not_found_cmd', cmd_)


menu_action = {'C': lambda name='', phone='', email='': controller.contact_create(name, phone, email),
               'R': lambda name='': controller.contact_read(name),
               'U': lambda name='', phone='', email='': controller.contact_update(name, phone, email),
               'D': lambda name='': controller.contact_delete(name),
               'A': controller.phonebook_read,
               'S': controller.phonebook_save,
               'H': controller.help_,
               'Q': controller.quit_,
               }

args = cmd_argpars.get_args()

#args.cmd = 'c'
#args.name = 'ron3'
#args.phone = 333444555

try:
    notifier.notify('hello')
    controller.phonebook_load()
    if args.cmd:
        menu_action.get(args.cmd.upper(), not_found_cmd(args.cmd.upper()))(args.name.upper(),
                                                                           args.phone,
                                                                           args.email,
                                                                           )
    else:
        while True:
            cmd = inputs.input_cmd()
            menu_action.get(cmd, not_found_cmd(cmd))()
finally:
    controller.phonebook_save()
    notifier.notify('exit')

