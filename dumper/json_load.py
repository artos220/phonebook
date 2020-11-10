import json


def load(dump_file):
    with open(dump_file, 'rt') as f:
        return json.load(f)
