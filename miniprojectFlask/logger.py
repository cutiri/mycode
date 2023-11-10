from datetime import datetime

class Logger:
    def __init__(self) -> None:
        pass

    def log(self, message):
        print("{0}: {1}".format(datetime.now(), message))