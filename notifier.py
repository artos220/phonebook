import messages as constants

print_ = print

messages = {
    'value_not_digit': lambda val: print_(constants.MSG_VALUE_NOT_DIGIT.format(val)),
    'start_without_data': lambda: print_(constants.MSG_CANT_LOAD_FILE, constants.MSG_START_WITHOUT_DATA),
    'input_some_data': lambda: print_(constants.MSG_INPUT_SOME_DATA),
    'contact_action': lambda action, name, phone: print_(constants.MSG_ACTION_WITH_CONTACT.format(action, name, phone)),
    'not_found': lambda name: print_(constants.MSG_NOT_FOUND_NAME.format(name)),
    'delete': lambda name: print_(constants.MSG_NAME_DELETE.format(name)),
    'contact': lambda name, phone: print_(constants.MSG_NAME_PHONE.format(name, phone)),
    'phonebook_saved': lambda: print_(constants.MSG_SAVE_PHONEBOOK),
    'phonebook_not_saved': lambda: print_(constants.MSG_ERROR_SAVE),
    'phonebook_loaded': lambda: print_(constants.MSG_LOAD_PHONEBOOK),
    'help': lambda: print_(constants.HELP),
    'not_found_cmd': lambda cmd: print_(constants.MSG_NOT_FOUND_CMD.format(cmd)),
    'hello': lambda: print_(constants.MSG_HELLO),
    'exit': lambda: print_(constants.MSG_EXIT_FROM_PROGRAM),
}


def notify(msg_type: str, *args):
    """print predefined message for msg_type and pass into it args"""
    messages[msg_type](*args)
