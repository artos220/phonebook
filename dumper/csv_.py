import csv


class CsvDumper:
    def __init__(self, dump_file):
        self.dump_file = dump_file

    def load(self):
        with open(self.dump_file, 'rt') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_MINIMAL)
            data = {}
            key = 0
            value = 1
            for row in reader:
                data[row[key]] = row[value]
            return data.copy()

    def save(self, data):
        with open(self.dump_file, 'wt') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            for name, value in data.items():
                writer.writerow([name, value])
