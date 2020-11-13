# class Contact not yet use
class Contact:
    def __init__(self, name, phone, email=''):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}'

    def __repr__(self):
        return f'{self.name}, {self.phone}, {self.email}'


class Phonebook:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def contact_create(self, contact):
        self.phonebook[contact[0]] = contact[1:]

    def contact_get(self, name):
        return self.phonebook[name]

    def contact_update(self, contact):
        self.phonebook[contact[0]] = contact[1:]

    def contact_delete(self, name):
        del self.phonebook[name]

    def phonebook_get(self):
        return self.phonebook

    def phonebook_set(self, data):
        self.phonebook = data

    def contact_exists(self, name) -> bool:
        return name in self.phonebook
