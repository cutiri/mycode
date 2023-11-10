import item, room, gate, command, unit, gamestatus, textcolor as color
import gameInitializer
import pprint

class StarCraft:
    def __init__(self):
        self.gameStatus = None
        self.initializer = None
        self.start_game()

        helpCommand = command.Command("help", self.helpCommand, "It will display this help menu")
        goCommand = command.Command("go", self.goCommand, "Go to a direction. e.g. 'go south'")
        getCommand = command.Command("get", self.getCommand, "You will get an object from the room. e.g. 'get key'")
        attackCommand = command.Command("attack", self.attackCommand, "You will attack an enemy unit. e.g. 'attack zerglingsassist'")
        assistCommand = command.Command("assist", self.assistCommand, "You will assist an ally unit. e.g. 'assist medic'")
        cheatCommand = command.Command("cheat", self.cheatCommand, "Don't do it Jimmy! She is a monster!")

        self.commands = {
            goCommand.trigger: goCommand,
            getCommand.trigger: getCommand,
            attackCommand.trigger: attackCommand,
            assistCommand.trigger: assistCommand,
            helpCommand.trigger: helpCommand,
            cheatCommand.trigger: cheatCommand,
        }

    def are_we_dead(self):
        return self.gameStatus.hp <= 0
    
    def have_we_won(self):
        return len(self.initializer.finalRoom.units) == 0

    def autocomplete(self, param):
        
        moveList = param.lower().split(" ", 1)
        action = moveList[0]
        target = moveList[1] if len(moveList) > 1 else ""

        if action and not target:
            keys = [item for item in self.commands.keys() if item.startswith(action) and item != action]
            result = { "results": keys}
            return result
        if target:
            if action == 'go':
                results = [(action + " " + obj.direction) for obj in self.gameStatus.currentRoom.gates]
                return { "results": results}
            if action == 'get':
                results = [(action + " " + obj.name) for obj in self.gameStatus.currentRoom.items]
                return { "results": results}
            if action == 'attack':
                results = [(action + " " + obj.name) for obj in self.gameStatus.currentRoom.getEnemies()]
                return { "results": results}
            if action == 'assist':
                results = [(action + " " + obj.name) for obj in self.gameStatus.currentRoom.getAllies()]
                return { "results": results}
        return None
        

    def execute_command(self, command):
        moveList = command.lower().split(" ", 1)
        action = moveList[0]
        target = moveList[1] if len(moveList) > 1 else ""
        
        if action in self.commands:
            self.gameStatus.message = self.commands[action].method(target)
        else:
            self.gameStatus.message = [action + " is not a valid command"]
        return self.gameStatus

    def start_game(self):
        self.initializer = gameInitializer.GameInitializer()
        self.gameStatus = gamestatus.GameStatus()
        self.gameStatus.currentRoom = self.initializer.mainRoom
        self.gameStatus.image = self.initializer.mainRoom.image
        return self.gameStatus

    ################################ COMMANDS ########################################
    ### ALL COMMANDS WILL RETURN THE MESSAGE
    def goCommand(self, param):
        gate = self.gameStatus.currentRoom.getGateByName(param)
        if gate:
            if gate.canOpen(self.gameStatus.inventory):
                nextRoom = self.gameStatus.currentRoom.getGateByName(param).room
                self.gameStatus.currentRoom = nextRoom
                self.gameStatus.image = nextRoom.image
                return []
            else:
                return ["You can't go there..."]
        else:
            return ["That is not a valid direction, try again."]

    def getCommand(self, param):
        item = self.gameStatus.currentRoom.getItemByName(param)
        if item:
            self.gameStatus.inventory.append(item)
            self.gameStatus.currentRoom.items.remove(item)
            return item.message
        else:
            return ["There is nothing with that name"]
            
    
    def attackCommand(self, param):
        targetUnit = self.gameStatus.currentRoom.getUnitByName(param)
        if not targetUnit:
            #self.message = ["Are you sure you typed that right?"]
            return ["Are you sure you typed that right?"]
        elif targetUnit.isFriendly:
            #self.message = ["You can't attack allied units, are you out of your mind?"]
            return ["You can't attack allied units, are you out of your mind?"]
        elif not targetUnit.attack(self.gameStatus.inventory, self.gameStatus.companions):
            self.gameStatus.hp = -1
            return targetUnit.failedInteractionMessage
        else:
            self.gameStatus.currentRoom.units.remove(targetUnit)
            self.gameStatus.currentRoom.items += targetUnit.drop
            #self.message = targetUnit.successfulInteractionMessage
            return targetUnit.successfulInteractionMessage

    def assistCommand(self, param):
        targetUnit = self.gameStatus.currentRoom.getUnitByName(param)
        if not targetUnit:
            #self.message = ["Are you sure you typed that right?"]
            return ["Are you sure you typed that right?"]
        elif not targetUnit.isFriendly:
            #self.message = ["You can't assist enemy units"]
            return ["You can't assist enemy units"]
        elif not targetUnit.assist(self.gameStatus.inventory):
            #self.message = targetUnit.failedInteractionMessage
            return targetUnit.failedInteractionMessage
        else:
            self.gameStatus.companions.append(targetUnit)
            self.gameStatus.currentRoom.units.remove(targetUnit)
            for item in targetUnit.needs:
                self.gameStatus.inventory.remove(item)
            #self.message = targetUnit.successfulInteractionMessage
            return targetUnit.successfulInteractionMessage

            

    def helpCommand(self, param):
        message = ["--------------------------------------------------------------------------"]
        
        for key, value in self.commands.items():
            message.append('<b>'+ key + ": </b>" + value.help)
        message.append("--------------------------------------------------------------------------")
        return message
    
    def cheatCommand(self, param):
        if param.lower() == "show me the money":
            self.gameStatus.inventory = self.gameStatus.inventory + self.initializer.items
            self.gameStatus.companions = self.gameStatus.companions + self.initializer.companions
            return ["Get all those items and companions."]
        if param.lower() == "there is no cow level":
            self.gameStatus.currentRoom = self.initializer.finalRoom
            return ["Go! Go! Go!"]
        return ["You can't even cheat right"]
    ################################ COMMANDS ########################################


if __name__ == "__main__":
    obj1 = StarCraft()
    print(obj1.execute_command("go down").convert_to_JSON())