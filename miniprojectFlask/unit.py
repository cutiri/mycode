
"""
The Unit class represents friendly or enemy units, could have done a Unit class and then two child classes Enemy and Friendly
"""
class Unit:
    def __init__(self, name, isFriendly, killableByUnit, killableByItem, successfulInteractionMessage, failedInteractionMessage, drop, needs) -> None:
        self.name = name
        self.isFriendly = isFriendly
        self.killableByUnit = killableByUnit
        self.killableByItem = killableByItem
        #successful interaction would be successfully killing an enemy or assisting a friendly
        self.successfulInteractionMessage = successfulInteractionMessage
        #failed interactiong would be failing to kill an enemy or assisting a friendly
        self.failedInteractionMessage = failedInteractionMessage
        self.drop = drop
        self.needs = needs
        pass

    def attack(self, inventory, companions):
        if self.isFriendly:
            return False
        if self.killableByItem and self.killableByItem not in inventory:
                return False
        if self.killableByUnit and self.killableByUnit not in companions:
                return False
        return True
    
    #gets executed when trying to assist
    def assist(self, inventory):
        if not self.isFriendly:
            return False
        for need in self.needs:
            if need not in inventory:
                return False
        return True
    
    #Operator overloads:
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name.lower() == other
        return self.name.lower() == other
        
    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name
    


    