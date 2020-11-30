import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-cmd", help="CRUD")
parser.add_argument("-name", help="contact name")
parser.add_argument("-phone", help="contact phone", default="")
parser.add_argument("-email", help="contact email", default="")
parser.add_argument("-h", help="start_phonebook.py -cmd=c -name=Test -phone=111000222", default="")


def parse_args(parser):
    return parser.parse_args()


def get_args():
    return parse_args(parser)
