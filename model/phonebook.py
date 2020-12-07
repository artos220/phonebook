from model.contact import Contact


class Phonebook:
    def __init__(self, phonebook: {}):
        self.phonebook = phonebook

    def get(self) -> {}:
        return self.phonebook.copy()

    def set(self, data: {}):
        self.phonebook = data.copy()

    def create_contact(self):
        contact = Contact()
        if contact.name in self.phonebook:
            raise KeyError
        contact.set_attr()
        self.phonebook[contact.name] = contact.contacts
        return contact

    def update_contact(self):
        contact = Contact()
        if contact.name not in self.phonebook:
            raise KeyError
        contact.set_attr()
        self.phonebook[contact.name] = contact.contacts
        return contact

    def __setitem__(self, name, attr):
        self.phonebook[name] = attr

    def __getitem__(self, name):
        return self.phonebook[name]

    def __delitem__(self, name):
        del self.phonebook[name]

    def __iter__(self):
        return iter(self.phonebook)

    def __contains__(self, name):
        return name in self.phonebook

    def __repr__(self):
        return repr(self.phonebook)

    def __copy__(self):
        return self.phonebook.copy()

    def items(self):
        return self.phonebook.items()
