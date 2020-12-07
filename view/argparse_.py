class ArgParse:
    def __init__(self, parser):
        self.parser = parser

    def parse_args(self):
        return self.parser.parse_args()
