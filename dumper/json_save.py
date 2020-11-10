import json


def save(data, dump_file):
    with open(dump_file, 'wt') as f:
        return json.dump(data, f)
