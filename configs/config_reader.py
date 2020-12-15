import configparser

config = configparser.ConfigParser()
reader = config.read('config.ini')

DUMP_TYPE = config['COMMON']['DUMP_TYPE']
DUMP_FILE = config['COMMON']['DUMP_FILE']
INPUT_TYPE = config['COMMON']['INPUT_TYPE']
INPUT_MODE = config['COMMON']['INPUT_MODE']
