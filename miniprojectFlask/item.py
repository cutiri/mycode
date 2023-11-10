class Item:
    def __init__(self, name, description, message) -> None:
        self.name = name
        self.description = description
        self.message = message
        pass

    #Overloading the == operator, comparing by Item.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return self.name.lower() == other

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name
    
    def to_dict(self):
        return {
            'name': self.name, 
            'description': self.description,
            'message': [obj for obj in self.message],
            #'enterRequirements': self.enterRequirements
        }