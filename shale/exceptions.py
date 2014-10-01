class ShaleException(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "{}(message={})".format(type(self).__name__, self.message)

