# Author: Artem Osmina
# Description: Simple Phone Book

pbk = {'JHON': 123456789,
       'PETROV': 333555777,
       'MARIA': 222444666,
       }

print('C - create\n'
      'R - read\n'
      'U - update\n'
      'D - delete')

while True:
    print('----')
    cmd = input('Input CRUD command letter:').strip().upper()
    if cmd not in 'CRUD':
        continue

    if cmd == 'C':
        name = input('Input name:').strip().upper()
        if pbk.get(name):
            print('{0} already exists'.format(name))
        else:
            phone = input('Input phone:').strip().upper()
            pbk[name] = phone

    elif cmd == 'R':
        name = input('Input name:').strip().upper()
        if pbk.get(name):
            print('{0} phone: {1}'.format(name, (pbk[name])))
        else:
            print('Not found: {0}'.format(name))

    elif cmd == 'U':
        name = input('Input name:').strip().upper()
        if pbk.get(name):
            print('{0} phone: {1}'.format(name, pbk[name]))

            phone = input('Input new phone:')
            pbk[name] = phone
        else:
            print('Not found: {0}'.format(name))

    elif cmd == 'D':
        name = input('Input name:').strip().upper()
        if pbk.get(name):
            pbk.pop(name)
            print('Deleted: {0}'.format(name))
        else:
            print('Not found: {0}'.format(name))
