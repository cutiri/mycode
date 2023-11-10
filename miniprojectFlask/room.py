import gate, item

class Room:
    def __init__(self, name, description, items, units, image) -> None:
        self.name = name
        self.description = description
        self.items = items
        self.units = units
        self.gates = []
        self.rooms = []
        self.enterRequirements = []
        self.hiddenUnless = []
        self.image = image
        pass

    def to_dict(self):
        return {'name': self.name, 
                'description': self.description,
                'items': [item.to_dict() for item in self.items],
                'units': [obj.name for obj in self.units],
                #'enterRequirements': self.enterRequirements
                }
    
    def getEnemies(self):
        return [obj for obj in self.units if not obj.isFriendly]
    
    def getAllies(self):
        return [obj for obj in self.units if obj.isFriendly]

    def addRoom(self, room):
        self.rooms.append(room)

    def addGate(self, gate):
        self.gates.append(gate)
    
    def addItem(self, item):
        self.items.append(item)

    def getItemsAsString(self):
        return self.items
    
    def getGateByName(self, gateName):
        for gate in self.gates:
            if gate.direction == gateName:
                return gate
        return None
    
    def getItemByName(self, itemName):
        for item in self.items:
            if item.name.lower() == itemName:
                return item
        return None
    
    def getUnitByName(self, unitName):
        for unit in self.units:
            if unit == unitName:
                return unit
        return None
    
    def getVisibleGates(self, inventory):
        #return list(filter(lambda obj: gate.isVisible(inventory) == True, self.gates))
        result = []
        for gate in self.gates:
            if gate.isVisible(inventory):
                result.append(gate)
        return result
    
    def getPossibleDestinationNames(self, inventory):
        destinations = ''
        visibleGates = self.getVisibleGates(inventory)
        lenght = len(visibleGates)

        if lenght == 0:
            return ""
        if lenght == 1:
            return visibleGates[0].direction
        destinations = visibleGates[0].direction        
        for i in range(1, lenght - 1):
            destinations += ', ' + visibleGates[i].direction
        destinations += " or " + visibleGates[-1].direction
        return destinations


    def canShow(self, inventory):
        # Check if every item in open_requirements exists in inventory
        all_exist = all(item in self.hiddenUnless for item in inventory)
        #return all_exist == True
        if all_exist:
            return True
        else:
            return False
    
    def canEnter(self, inventory):
        # Check if every item in open_requirements exists in inventory
        all_exist = all(item in self.enterRequirements for item in inventory)
        #return all_exist == True
        if all_exist:
            return True
        else:
            return False
        
    def getAllyUnits(self):
        return [unit for unit in self.units if unit.isFriendly]
    
    def getEnemyUnits(self):
        return [unit for unit in self.units if not unit.isFriendly]

if __name__ == "__main__":
    item = item.Item("key", "No desc", "Just a key")
    room1 = Room("Living", "Just the living", [], [])
    room2 = Room("Kitchen", "Just the kitchen", [], [])

    #gate = gate.Gate("east", )
    print(room1.getPossibleDestinationNames([]))