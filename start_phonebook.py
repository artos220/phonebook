# Author: Artem Osmina
# Description: Simple Phone Book

# phone book
phonebook = {'JHON': '123456789123',
             'MARIA': '222444666888',
            }

# Messages for print
MSG_NOT_FOUND_NAME = 'Not found name: "{0}"'
MSG_OPERATION_WITH_CONTACT = '{0} contact name: "{1}" phone: {2}'
MSG_VALUE_NOT_DIGIT = 'Value: {0} is not digit'
MSG_NAME_DELETE = 'Delete name: "{0}"'
MSG_NAME_PHONE = 'Name: {0} phone: {1}'
MSG_NOT_FOUND_CMD = 'Not found command: {0}'
MSG_INPUT_CMD = 'input command:'
MSG_INPUT_NAME = 'input name:'
MSG_INPUT_PHONE = 'input phone:'
MSG_INPUT_SOME_DATA = 'Please input some data'
HELP = '''
C name phone - create contact
R name - get phone
U name phone - update contact
D name - delete contact
A - list all contacts
H - this help
Q - quit
'''


# repeat input if empty
def loop_if_empty_result(fn):
    def wrapper():
        while True:
            val = fn()
            if len(val) > 0:
                return val
                break
            else:
                print(MSG_INPUT_SOME_DATA)
    return wrapper


def strip_upp(fn):
    def wrapper():
        return fn().strip().upper()
    return wrapper


def try_input(fn):
    def wrapper():
        try:
            return fn()
        except Exception as e:
            print(e)
            # except KeyboardInterrupt don't work
            # raise KeyboardInterrupt
    return wrapper


@loop_if_empty_result
@strip_upp
@try_input
def input_cmd() -> str:
    return input(MSG_INPUT_CMD)


@loop_if_empty_result
@strip_upp
@try_input
def input_name() -> str:
    return input(MSG_INPUT_NAME)


@loop_if_empty_result
@strip_upp
@try_input
def input_phone() -> str:
    phone = input(MSG_INPUT_PHONE)
    if phone.isdigit():
        return phone
    else:
        print(MSG_VALUE_NOT_DIGIT.format(phone))
        return ''


def phonebook_get(name, command='Found') -> str:
    if phonebook.get(name):
        print(MSG_OPERATION_WITH_CONTACT.format(command, name, phonebook.get(name)))
        return phonebook.get(name)
    else:
        print(MSG_NOT_FOUND_NAME.format(name))
        return False


def create():
    name = input_name()
    if not phonebook_get(name):
        phonebook[name] = input_phone()
        phonebook_get(name, 'Create')


def read():
    name = input_name()
    phonebook_get(name)


def update():
    name = input_name()
    if phonebook_get(name):
        phonebook[name] = input_phone()
        phonebook_get(name, 'Update')


def delete():
    name = input_name()
    if phonebook_get(name):
        phonebook.pop(name)
        print(MSG_NAME_DELETE.format(name))


def read_all():
    for name, value in phonebook.items():
        print(MSG_NAME_PHONE.format(name, value))


def print_help():
    print(HELP)


def quit_():
    # exit()
    raise KeyboardInterrupt


action_menu = {'C': create,
               'R': read,
               'U': update,
               'D': delete,
               'A': read_all,
               'H': print_help,
               'Q': quit_,
               }


while True:
    print('----')
    cmd = input_cmd()
    fn_action = action_menu.get(cmd)
    if fn_action:
        fn_action()
    else:
        print(MSG_NOT_FOUND_CMD.format(cmd))
