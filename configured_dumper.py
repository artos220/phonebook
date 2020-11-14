import config_reader as config


if config.DUMP_TYPE.lower() == 'json':
    from dumper.JsonDumper import JsonDumper as DataDumper
elif config.DUMP_TYPE.lower() == 'pickle':
    from dumper.PickleDumper import PickleDumper as DataDumper
elif config.DUMP_TYPE.lower() == 'csv':
    from dumper.CsvDumper import CsvDumper as DataDumper


def load(filename):
    return DataDumper.load(filename)


def save(data, filename):
    return DataDumper.save(data, filename)
