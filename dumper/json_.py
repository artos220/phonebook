import json


class JsonDumper:
    def __init__(self, dump_file):
        self.dump_file = dump_file

    def load(self):
        with open(self.dump_file, 'rt') as f:
            return json.load(f).copy()

    def save(self, data):
        with open(self.dump_file, 'wt') as f:
            return json.dump(data, f)
