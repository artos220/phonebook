from view import notifier
from configs import config_reader as config, configured_dumper as dumper
from model import phonebook
from model.contact import Name

phonebook = phonebook.Phonebook({})


def contact_create():
    contact = phonebook.create_contact()
    notifier.notify('contact_action', 'Create', contact.name, contact.contacts)


def contact_read():
    try:
        name = Name().value
        contact_found_notify(name)
    except KeyError:
        pass


def contact_update():
    try:
        contact = phonebook.update_contact()
        notifier.notify('contact_action', 'Update', contact.name, contact.contacts)
    except KeyError:
        pass


def contact_delete():
    try:
        name = Name().value
        contact_found_notify(name)
        del phonebook[name]
        notifier.notify('delete', name)
    except KeyError:
        pass


def contact_found_notify(name):
    try:
        contacts = phonebook[name]
        notifier.notify('contact_action', 'Found', name, contacts)
    except KeyError:
        notifier.notify('not_found', name)
        raise


def phonebook_read():
    for name, value in phonebook.items():
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
