import notifier
import inputs
import config_reader as config
import configured_dumper as dumper
from model import Phonebook, Contact

phonebook = Phonebook({})


def contact_found_notify(name):
    try:
        phone = phonebook.contact_get(name)
        notifier.notify('contact_action', 'Found', name, phone)
    except KeyError:
        notifier.notify('not_found', name)
        raise


def contact_create():
    try:
        name = inputs.input_name()
        contact_found_notify(name)
    except KeyError:
        phone = inputs.input_phone()
        email = inputs.input_email()
        phonebook.contact_create(Contact(name, phone, email))
        notifier.notify('contact_action', 'Create', name, phone)


def contact_read():
    try:
        name = inputs.input_name()
        contact_found_notify(name)
    except KeyError:
        pass


def contact_update():
    try:
        name = inputs.input_name()
        contact_found_notify(name)
        phone = inputs.input_phone()
        email = inputs.input_email()
        phonebook.contact_update(Contact(name, phone, email))
        notifier.notify('contact_action', 'Update', name, phone)
    except KeyError:
        pass


def contact_delete():
    try:
        name = inputs.input_name()
        contact_found_notify(name)
        phonebook.contact_delete(name)
        notifier.notify('delete', name)
    except KeyError:
        pass


def phonebook_read():
    for name, value in phonebook.get().items():
        notifier.notify('contact', name, value)


def phonebook_load():
    try:
        phonebook.set(dumper.load(config.DUMP_FILE))
        notifier.notify('phonebook_loaded')
    except FileNotFoundError:
        notifier.notify('start_without_data')


def phonebook_save():
    try:
        dumper.save(phonebook.get(), config.DUMP_FILE)
        notifier.notify('phonebook_saved')
    except Exception:
        notifier.notify('phonebook_not_saved')
        raise


def help_():
    notifier.notify('help')


def quit_():
    # exit() # pycharm catch exit exception
    raise KeyboardInterrupt
