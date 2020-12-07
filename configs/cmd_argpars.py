import argparse
from view.argparse_ import ArgParse

parser = argparse.ArgumentParser()
parser.add_argument("-cmd", help="CRUD")
parser.add_argument("-name", help="contact name")
parser.add_argument("-phone", help="contact phone", default="")
parser.add_argument("-email", help="contact email", default="")
parser.add_argument("-help", help="start_phonebook.py -cmd=c -name=Test -phone=111000222", default="")


args = ArgParse(parser)
