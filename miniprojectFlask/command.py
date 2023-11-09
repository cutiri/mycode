class Command:
    def __init__(self, trigger:str, method:str, help:str) -> None:
        self.trigger = trigger
        self.method = method
        self.help = help
        pass