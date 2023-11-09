import room, item

class Gate:
    def __init__(self, direction, room, openRequirements, visibleRequirements) -> None:
        self.room = room
        self.direction = direction
        self.openRequirements = openRequirements
        self.visibleRequirements = visibleRequirements
        pass

    #Can we open the room? A room may have a required item to be able to open it, so we check if that item is in the inventory
    def canOpen(self, inventory):
        for item in self.openRequirements:
            if not any(obj.name == item.name for obj in inventory):
                return False
        return True
    
    #Check if the gate is visible, a gate may be visible only if we have a required item in our inventory
    def isVisible(self, inventory):
        return all(item in inventory for item in self.visibleRequirements)

    #a regular setter
    def setRoom(self, room):
        self.room = room



if __name__ == "__main__":
    key = item.Item("key", "", "")
    gate = Gate("south", None, [key], [key])

    #print(gate.isVisible(["key"]))
    #print(gate.isVisible(["bread", "key"]))
    #print(gate.isVisible([]))
    
    print(gate.canOpen([key]))
    print(gate.canOpen([]))
