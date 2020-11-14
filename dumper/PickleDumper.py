import pickle


class PickleDumper:
    def __init__(self, dump_file):
        self.dump_file = dump_file

    def load(self):
        with open(self.dump_file, 'rb') as f:
            return pickle.load(f)

    def save(self, data):
        with open(self.dump_file, 'wb') as f:
            return pickle.dump(data, f)
