import configparser

config = configparser.ConfigParser()
reader = config.read('config.ini')

DUMP_TYPE = config['COMMON']['DUMP_TYPE']
DUMP_FILE = config['COMMON']['DUMP_FILE']
