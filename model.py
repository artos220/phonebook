class Contact:
    def __init__(self, name, phone, email=''):
        self.name = name
        self.phone = phone
        self.email = email

    def props_get(self):
        return [self.phone, self.email]

    def name_get(self):
        return self.name

    def __repr__(self):
        return f'Contact(name={self.name}, phone={self.phone}, email={self.email})'


class Phonebook:
    def __init__(self, phonebook: {}):
        self.phonebook = phonebook

    def contact_create(self, contact: Contact):
        self.phonebook[contact.name_get()] = contact.props_get()

    def contact_get(self, name):
        return self.phonebook[name]

    def contact_update(self, contact: Contact):
        self.phonebook[contact.name_get()] = contact.props_get()

    def contact_delete(self, name):
        del self.phonebook[name]

    def get(self) -> {}:
        return self.phonebook.copy()

    def set(self, data: {}):
        self.phonebook = data.copy()

    def contact_exists(self, name) -> bool:
        return name in self.phonebook
