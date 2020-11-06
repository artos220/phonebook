import notifications
import inputs
import model


def contact_exists_notify(name):
    try:
        notifications.notify('contact_action', 'Found', name, model.contact_get(name))
    except KeyError:
        notifications.notify('not_found', name)
        raise


def contact_create():
    name = inputs.input_name()
    try:
        contact_exists_notify(name)
    except KeyError:
        phone = inputs.input_phone()
        model.contact_create(name, phone)
        notifications.notify('contact_action', 'Create', name, phone)


def contact_read():
    name = inputs.input_name()
    try:
        contact_exists_notify(name)
    except KeyError:
        pass


def contact_update():
    name = inputs.input_name()
    try:
        contact_exists_notify(name)
        phone = inputs.input_phone()
        model.contact_update(name, phone)
        notifications.notify('contact_action', 'Update', name, phone)
    except KeyError:
        pass


def contact_delete():
    name = inputs.input_name()
    try:
        contact_exists_notify(name)
        model.contact_delete(name)
        notifications.notify('delete', name)
    except KeyError:
        pass


def phonebook_read():
    for name, value in model.phonebook_get().items():
        notifications.notify('contact', name, value)


def phonebook_load():
    try:
        model.phonebook_load()
        notifications.notify('phonebook_loaded')
    except FileNotFoundError:
        notifications.notify('start_without_data')


def phonebook_save():
    try:
        model.phonebook_save()
        notifications.notify('phonebook_saved')
    except Exception:
        notifications.notify('phonebook_not_saved')
        raise


def help_():
    notifications.notify('help')


def quit_():
    # exit() # pycharm catch exit exception
    raise KeyboardInterrupt
