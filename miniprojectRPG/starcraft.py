import room, gate, item, unit, os, command, gameInitializer, textcolor as color



class StarCraftRPG:

    def __init__(self) -> None:
        helpCommand = command.Command("help", self.helpCommand, "It will display this help menu")
        goCommand = command.Command("go", self.goCommand, "Go to a direction. e.g. 'go south'")
        getCommand = command.Command("get", self.getCommand, "You will get an object from the room. e.g. 'get key'")
        attackCommand = command.Command("attack", self.attackCommand, "You will attack an enemy unit. e.g. 'attack zerglingsassist'")
        assistCommand = command.Command("assist", self.assistCommand, "You will assist an ally unit. e.g. 'assist medic'")
        cheatCommand = command.Command("cheat", self.cheatCommand, "Don't do it Jimmy! She is a monster!")

        self.init = gameInitializer.GameInitializer()

        self.currentRoom = self.init.mainRoom
        self.inventory = []
        self.commands = {
            goCommand.trigger: goCommand,
            getCommand.trigger: getCommand,
            attackCommand.trigger: attackCommand,
            assistCommand.trigger: assistCommand,
            helpCommand.trigger: helpCommand,
            cheatCommand.trigger: cheatCommand,
        }
        self.message = []
        self.companions = []
        self.color = color.Color()

        

    def showStatus(self):
        print('---------------------------')
        print('You are in the ' + color.Color.RED +  self.currentRoom.name + color.Color.RESET)
        print(color.Color.PURPLE + self.currentRoom.description)
        # print what the player is carrying
        print('Inventory:', self.inventory)
        # check if there's an item in the room, if so print it
        print('You see: ', self.currentRoom.getItemsAsString())
        print('Available directions: ', self.currentRoom.getPossibleDestinationNames(self.inventory))
        print('Ally units: ', self.currentRoom.getAllyUnits())
        print('Enemy units: ', self.currentRoom.getEnemyUnits())
    
    def runGame(self):
        
        print("")
        while True:
            os.system('cls')
            os.system('clear')
            self.printMessage(self.message)
            self.message = []
            self.showStatus()

            move = ''
            while move == '':  
                move = input('>')

            moveList = move.lower().split(" ", 1)
            action = moveList[0]
            target = moveList[1] if len(moveList) > 1 else ""
            self.commands[action].method(target)


    ##### COMMANDS: ######

    def goCommand(self, param):
        print("go with param" + param)
        gate = self.currentRoom.getGateByName(param)
        if gate:
            if gate.canOpen(self.inventory):
                self.currentRoom = self.currentRoom.getGateByName(param).room
            else:
                self.message = ["You can't go there..."]

    def getCommand(self, param):
        print('get with param' + param)
        item = self.currentRoom.getItemByName(param)
        if item:
            self.inventory.append(item)
            self.currentRoom.items.remove(item)
            self.message = item.message
        else:
            self.message = ["There is nothing with that name"]
            
    
    def attackCommand(self, param):
        print('attack with param' + param)

    def assistCommand(self, param):
        targetUnit = self.currentRoom.getUnitByName(param)
        if not targetUnit:
            self.message = ["Are you sure you typed that right?"]
        elif not targetUnit.isFriendly:
            self.message = ["You can't assist enemy units"]
        elif not targetUnit.assist():
            self.message = ["You are missing an item to assist ", targetUnit.name, " keep looking around."]
        else:
            self.message = [targetUnit.successfulInteractionMessage]
            self.companions.append(targetUnit)
            del self.currentRoom.units[targetUnit]
            

    def printMessage(self, message):
        for line in message:
            print(line)

    def helpCommand(self, param):
        self.message = ["--------------------------------------------------------------------------"]
        
        for key, value in self.commands.items():
            self.message.append(key + ": " + value.help)
        self.message.append("--------------------------------------------------------------------------")
    
    def cheatCommand(self, param):
        if param.lower() == "show me the money":
            self.inventory = self.inventory + self.init.items