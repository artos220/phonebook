phonebook = dict()


def contact_create(name, phone):
    phonebook[name] = phone


def contact_get(name):
    return phonebook[name]


def contact_update(name, phone):
    phonebook[name] = phone


def contact_delete(name):
    del phonebook[name]


def phonebook_get():
    return phonebook


def phonebook_set(data):
    global phonebook
    phonebook = data


def contact_exists(name) -> bool:
    if name in phonebook:
        return True
    return False
