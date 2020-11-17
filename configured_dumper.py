import config_reader as config


if config.DUMP_TYPE.lower() == 'json':
    from dumper.json_ import JsonDumper as DataDumper
elif config.DUMP_TYPE.lower() == 'pickle':
    from dumper.pickle_ import PickleDumper as DataDumper
elif config.DUMP_TYPE.lower() == 'csv':
    from dumper.csv_ import CsvDumper as DataDumper


def load(filename):
    return DataDumper(filename).load()


def save(data, filename):
    return DataDumper(filename).save(data)
