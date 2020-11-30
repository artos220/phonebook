import notifier
import config_reader as config
import configured_dumper as dumper
from model import Phonebook
from contact import Contact, Name, Phone, Email

phonebook = Phonebook({})


def contact_create(name, phone, email):
    contact = Contact(name, phone, email)
    phonebook.create_contact(contact)
    notifier.notify('contact_action', 'Create', contact.name, contact.contacts)


def contact_read(name):
    try:
        name = Name(name).value
        contact_found_notify(name)
    except KeyError:
        pass


def contact_update(name, phone, email):
    try:
        contact = Contact(name, phone, email)
        phonebook.update_contact(contact)
        notifier.notify('contact_action', 'Update', contact.name, contact.contacts)
    except KeyError:
        pass


def contact_delete(name):
    try:
        name = Name(name).value
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
