import pickle


class PickleDumper:
    def __init__(self, dumper_file):
        self.dumper_file = dumper_file

    def load(self):
        with open(self.dump_file, 'rb') as f:
            return pickle.load(f)

    def save(self, data):
        with open(self.dumper_file, 'wb') as f:
            return pickle.dump(data, f)
