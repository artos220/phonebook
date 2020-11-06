import load_dump
import config_reader as config
import messages as constants

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


def contact_exists(name) -> bool:
    if name in phonebook:
        return True
    return False


# transfer into package
if config.DUMP_TYPE.lower() == 'json':
    data_get, data_dump = load_dump.json_get, load_dump.json_dump
elif config.DUMP_TYPE.lower() == 'pickle':
    data_get, data_dump = load_dump.pickle_get, load_dump.pickle_dump
else:
    ValueError(constants.MSG_UNKNOWN_DUMP_TYPE.format(config.DUMP_TYPE))  # hmm ?


def phonebook_save():
    return data_dump(phonebook, config.DUMP_FILE) # transfer parameter DUMP_FILE into package


def phonebook_load():
    global phonebook
    try:
        phonebook = data_get(config.DUMP_FILE)
    except FileNotFoundError:
        phonebook = dict()
        raise