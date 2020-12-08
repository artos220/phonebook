import argparse


class ArgParse:
    def __init__(self, parser):
        self.parser = parser

    def parse_args(self):
        return self.parser.parse_args()


parser = argparse.ArgumentParser()
parser.add_argument("-cmd", help="CRUD")
parser.add_argument("-name", help="contact name")
parser.add_argument("-phone", help="contact phone", default="")
parser.add_argument("-email", help="contact email", default="")
parser.add_argument("-help", help="start_phonebook.py -cmd=c -name=Test -phone=111000222", default="")


args = ArgParse(parser)
