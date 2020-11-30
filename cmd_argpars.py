import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-cmd", help="")
parser.add_argument("-name", help="")
parser.add_argument("-phone", help="", default="")
parser.add_argument("-email", help="", default="")


def parse_args(parser):
    return parser.parse_args()


def get_args():
    return parse_args(parser)
