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
        self.hp = 100

    def printMessage(self):
        if len(self.message) > 0:
            print('---------------------------------------------------------------------------------')
            for line in self.message:
                print(line)

    def showStatus(self):
        print('---------------------------------------------------------------------------------')
        print('You are in the ' + color.Color.RED +  self.currentRoom.name + color.Color.RESET)
        print(color.Color.GREEN + self.currentRoom.description + color.Color.RESET)
        # print what the player is carrying
        print(color.Color.DARK_GRAY + 'Inventory:' + color.Color.RESET + str(self.inventory) )
        print(color.Color.DARK_GRAY + 'Companions:' + color.Color.RESET + str(self.companions) )
        # check if there's an item in the room, if so print it
        print(color.Color.DARK_GRAY + 'You see: ' + color.Color.RESET +  str(self.currentRoom.getItemsAsString()))
        print(color.Color.DARK_GRAY + 'Available directions: ' + color.Color.RESET + self.currentRoom.getPossibleDestinationNames(self.inventory))
        print(color.Color.DARK_GRAY + 'Ally units: ' + color.Color.RESET +  str(self.currentRoom.getAllyUnits()))
        print(color.Color.DARK_GRAY + 'Enemy units: ' + color.Color.RESET + str(self.currentRoom.getEnemyUnits()))
    
    def runGame(self):
        while self.hp > 0:
            os.system('cls')
            os.system('clear')
            self.printMessage()
            self.showStatus()
            self.message = []

            move = ''
            while move == '':  
                move = input('>')

            moveList = move.lower().split(" ", 1)
            action = moveList[0]
            target = moveList[1] if len(moveList) > 1 else ""
            self.commands[action].method(target)
            if self.init.winningConditionsMet():
                break
        
        self.endGame()

    ##### COMMANDS: ######

    def goCommand(self, param):
        gate = self.currentRoom.getGateByName(param)
        if gate:
            if gate.canOpen(self.inventory):
                self.currentRoom = self.currentRoom.getGateByName(param).room
            else:
                self.message = ["You can't go there..."]
        else:
            self.message = ["That is not a valid direction, try again."]

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
        targetUnit = self.currentRoom.getUnitByName(param)
        if not targetUnit:
            self.message = ["Are you sure you typed that right?"]
        elif targetUnit.isFriendly:
            self.message = ["You can't attack allied units, are you out of your mind?"]
        elif not targetUnit.attack(self.inventory, self.companions):
            self.message = targetUnit.failedInteractionMessage
            self.hp = -1
        else:
            self.message = targetUnit.successfulInteractionMessage
            self.currentRoom.units.remove(targetUnit)
            self.currentRoom.items += targetUnit.drop

    def assistCommand(self, param):
        targetUnit = self.currentRoom.getUnitByName(param)
        if not targetUnit:
            self.message = ["Are you sure you typed that right?"]
        elif not targetUnit.isFriendly:
            self.message = ["You can't assist enemy units"]
        elif not targetUnit.assist(self.inventory):
            self.message = targetUnit.failedInteractionMessage
        else:
            self.message = targetUnit.successfulInteractionMessage
            self.companions.append(targetUnit)
            self.currentRoom.units.remove(targetUnit)
            for item in targetUnit.needs:
                self.inventory.remove(item)
            

    def helpCommand(self, param):
        self.message = ["--------------------------------------------------------------------------"]
        
        for key, value in self.commands.items():
            self.message.append(key + ": " + value.help)
        self.message.append("--------------------------------------------------------------------------")
    
    def cheatCommand(self, param):
        if param.lower() == "show me the money":
            self.inventory = self.inventory + self.init.items
    
    def endGame(self):
        self.printMessage()
        if self.hp <= 0:
            print(self.init.looseMessage)
        if self.hp > 0:
            print(self.init.winningMessage)
        
        input("Press Enter to close the game...")
