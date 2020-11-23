class Phonebook:
    def __init__(self, phonebook: {}):
        self.phonebook = phonebook

    # what is the magic method get/set?
    def get(self) -> {}:
        return self.phonebook.copy()

    def set(self, data: {}):
        self.phonebook = data.copy()

    def __setitem__(self, name, contact):
        self.phonebook[contact.name] = contact.contacts

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
