import csv


def save(data, dump_file):
    with open(dump_file, 'wt') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        for name, value in data.items():
            writer.writerow([name, value])
