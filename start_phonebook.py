# Author: Artem Osmina
# Description: Simple Phone Book
# config and save/load contacts file

import configparser
import json
import pickle
from sys import exit

config = configparser.ConfigParser()
reader = config.read('config.ini')

DUMP_TYPE = config['COMMON']['DUMP_TYPE']
DUMP_FILE = config['COMMON']['DUMP_FILE']

messages = config['MESSAGES']
MSG_NOT_FOUND_NAME = messages['MSG_NOT_FOUND_NAME']
MSG_ACTION_WITH_CONTACT = messages['MSG_ACTION_WITH_CONTACT']
MSG_VALUE_NOT_DIGIT = messages['MSG_VALUE_NOT_DIGIT']
MSG_NAME_DELETE = messages['MSG_NAME_DELETE']
MSG_NAME_PHONE = messages['MSG_NAME_PHONE']
MSG_NOT_FOUND_CMD = messages['MSG_NOT_FOUND_CMD']
MSG_INPUT_CMD = messages['MSG_INPUT_CMD']
MSG_INPUT_NAME = messages['MSG_INPUT_NAME']
MSG_INPUT_PHONE = messages['MSG_INPUT_PHONE']
MSG_INPUT_SOME_DATA = messages['MSG_INPUT_SOME_DATA']
HELP = messages['HELP']
MSG_UNKNOWN_DUMP_TYPE = messages['MSG_UNKNOWN_DUMP_TYPE']
MSG_CANT_LOAD_FILE = messages['MSG_CANT_LOAD_FILE']
MSG_START_WITHOUT_DATA = messages['MSG_START_WITHOUT_DATA']
MSG_HELLO = messages['MSG_HELLO']
MSG_EXIT_FROM_PROGRAM = messages['MSG_EXIT_FROM_PROGRAM']
MSG_SAVE_PHONEBOOK = messages['MSG_SAVE_PHONEBOOK']
MSG_LOAD_PHONEBOOK = messages['MSG_LOAD_PHONEBOOK']

print_ = print
phonebook = dict()


def json_get(dump_file):
    with open(dump_file, 'rt') as f:
        return json.loads(f.read())


def pickle_get(dump_file):
    with open(dump_file, 'rb') as f:
        return pickle.loads(f.read())


def data_get(dump_type, dump_file):
    if dump_type == 'json':
        return json_get(dump_file)
    elif dump_type == 'pickle':
        return pickle_get(dump_file)
    raise ValueError(MSG_UNKNOWN_DUMP_TYPE.format(dump_type))


def json_dump(data, dump_file):
    with open(dump_file, 'wt') as f:
        return f.write(json.dumps(data))


def pickle_dump(data, file):
    with open(file, 'wb') as f:
        return f.write(pickle.dumps(data))


def data_dump(data, dump_type, dump_file):
    if dump_type == 'json':
        return json_dump(data, dump_file)
    elif dump_type == 'pickle':
        return pickle_dump(data, dump_file)
    raise ValueError(MSG_UNKNOWN_DUMP_TYPE.format(dump_type))


def loop_if_empty_result(fn):
    def wrapper():
        while True:
            val = fn()
            if val:
                return val
            print_input_some_data()
    return wrapper


@loop_if_empty_result
def input_cmd():
    return input(MSG_INPUT_CMD).strip().upper()


@loop_if_empty_result
def input_name():
    return input(MSG_INPUT_NAME).strip().upper()


@loop_if_empty_result
def input_phone():
    phone = input(MSG_INPUT_PHONE).strip().upper()
    if phone.isdigit():
        return phone
    print_value_not_digit(phone)


def print_value_not_digit(value):
    print_(MSG_VALUE_NOT_DIGIT.format(value))


def print_start_without_data():
    print_(MSG_CANT_LOAD_FILE, MSG_START_WITHOUT_DATA)


def print_input_some_data():
    print_(MSG_INPUT_SOME_DATA)


def print_contact_action(action, name, phone):
    print_(MSG_ACTION_WITH_CONTACT.format(action, name, phone))


def print_not_found(name):
    print_(MSG_NOT_FOUND_NAME.format(name))


def print_delete(name):
    print_(MSG_NAME_DELETE.format(name))


def print_contact(name, phone):
    print_(MSG_NAME_PHONE.format(name, phone))


def print_phonebook_saved():
    print_(MSG_SAVE_PHONEBOOK)


def print_phonebook_loaded():
    print_(MSG_LOAD_PHONEBOOK)


def print_help():
    print_(HELP)


def print_not_found_cmd(cmd):
    print_(MSG_NOT_FOUND_CMD.format(cmd))


def print_hello():
    print_(MSG_HELLO)


def print_exit():
    print_(MSG_EXIT_FROM_PROGRAM)


def contact_create(name, phone):
    if not contact_exists(name):
        phonebook[name] = phone


def contact_get(name):
    if contact_exists(name):
        return phonebook[name]


def contact_update(name, phone):
    if contact_exists(name):
        phonebook[name] = phone


def contact_delete(name):
    del phonebook[name]


def phonebook_get():
    return phonebook


def contact_exists(name):
    if name in phonebook:
        return True


def phonebook_save():
        return data_dump(phonebook, DUMP_TYPE, DUMP_FILE)


def phonebook_load():
    global phonebook
    try:
        phonebook = data_get(DUMP_TYPE, DUMP_FILE)
        return True
    except FileNotFoundError as e:
        phonebook = dict()


def contact_exists_notify_action(name):
    if contact_exists(name):
        print_contact_action('Found', name,  contact_get(name))
        return True
    print_not_found(name)


def contact_create_action():
    name = input_name()
    if not contact_exists_notify_action(name):
        phone = input_phone()
        contact_create(name, phone)
        print_contact_action('Create', name, phone)


def contact_read_action():
    name = input_name()
    contact_exists_notify_action(name)


def contact_update_action():
    name = input_name()
    if contact_exists_notify_action(name):
        phone = input_phone()
        contact_update(name, phone)
        print_contact_action('Update', name, phone)


def contact_delete_action():
    name = input_name()
    try:
        contact_delete(name)
        print_delete(name)
    except KeyError:
        print_not_found(name)


def phonebook_read_action():
    for name, value in phonebook_get().items():
        print_contact(name, value)


def phonebook_load_action():
    if phonebook_load():
        print_phonebook_loaded()
    else:
        print_start_without_data()


def phonebook_save_action():
    if phonebook_save():
        print_phonebook_saved()
    else:
        pass


def help_action():
    print_help()


def quit_action():
    # exit() # pycharm catch exit exception
    raise KeyboardInterrupt


menu_action = {'C': contact_create_action,
               'R': contact_read_action,
               'U': contact_update_action,
               'D': contact_delete_action,
               'A': phonebook_read_action,
               'S': phonebook_save_action,
               'H': help_action,
               'Q': quit_action,
               }

try:
    print_hello()
    phonebook_load_action()
    while True:
        cmd = input_cmd()
        menu_action.get(cmd, lambda: print_not_found_cmd(cmd))()
finally:
    phonebook_save_action()
    print_exit()
