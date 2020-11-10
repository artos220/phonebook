import config_reader as config


if config.DUMP_TYPE.lower() == 'json':
    from dumper import json_load as data_load
    from dumper import json_save as data_save
elif config.DUMP_TYPE.lower() == 'pickle':
    from dumper import pickle_load as data_load
    from dumper import pickle_save as data_save


def load(filename):
    return data_load.load(filename)


def save(data, filename):
    return data_save.save(data, filename)
