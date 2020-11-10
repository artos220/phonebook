import pickle


def load(dump_file):
    with open(dump_file, 'rb') as f:
        return pickle.load(f)
