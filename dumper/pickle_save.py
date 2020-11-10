import pickle


def save(data, file):
    with open(file, 'wb') as f:
        return pickle.dump(data, f)
