import json
import pickle


def json_get(dump_file):
    with open(dump_file, 'rt') as f:
        return json.load(f)


def pickle_get(dump_file):
    with open(dump_file, 'rb') as f:
        return pickle.load(f)


def json_dump(data, dump_file):
    with open(dump_file, 'wt') as f:
        return json.dump(data, f)


def pickle_dump(data, file):
    with open(file, 'wb') as f:
        return pickle.dump(data, f)
