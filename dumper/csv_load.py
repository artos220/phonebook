import csv


def load(dump_file):
    with open(dump_file, 'rt') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_MINIMAL)
        data = {}
        for row in reader:
            data[row[0]] = row[1]

        return data
