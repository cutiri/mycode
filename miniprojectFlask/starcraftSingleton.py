import item, room, gate, command, unit, gamestatus, textcolor as color
import pprint

class StarCraftSingleton:
    _instance = None  # Class variable to store the instance

    def __init__(self):
        khaydarin = item.Item("crystal", "A piece of Khaydarin Crystal, it's blue and shinny", ["You pick up the crystal, it is blue and shinny"])
        keycard = item.Item("Key Card", "A bloody key card, a name is still visible, it belonged to Edmund Duke", 
                            ["You pick up the card, it still has rests of blood on it and you can read a name Edmund Duke"])
        rifle = item.Item("rifle", "A C-14 Impaler gauss rifle, is the standard marine rifle", 
                          ["You pick up the C-14 Impaler Gauss rifle, the standard marine rifle in the Terran forces."])
        stimpack = item.Item("stimpack", "A brand new stimpack never used", 
                             ["You pick up a Medic's stimpack, commonly used among Terran forces to revive injured soldiers."])

        

        firebat = unit.Unit("Firebat", True, None, None, 
                            ["You quickly use the stimpack on the firebat and this one inmediatly stands up fuelled by the drug and yells",
                             color.Color.PURPLE + "Fueled up! Ready to roast!" + color.Color.RESET], 
                            ["You need something else"], [], [stimpack])
        marine = unit.Unit("Marine", True, None, None, 
                           ["You quickly use the stimpack on the marine and this one inmediatly stands up fuelled by the drug and yells"
                            , color.Color.RED + "Oh yeeaaahh... Go ahead commander." + color.Color.RESET],
                            ["You need something else"], [], [stimpack])
        zerglings = unit.Unit("Zerglings", False, firebat, None, 
                              ["With a swift, precise sweep of his flamethrower",
                               "your fellow Firebat incinerates the charging Zerglings",
                               "turning them into ashes in the blink of an eye.",
                               "Then you see a keycard one of them was chewing."], 
                              ["You start shooting at the Zerglings but they are too many and soon overwealm you",
                               "one of them is able to reach you and stab you in the chest",
                               "you fall to the ground and soon loose conciousness."],
                              [keycard], [])
        hydralisk = unit.Unit("Hydralisk", False, None, rifle, 
                              ["As you aim your C-14 Impaler at the Hydralisk and open fire, the hideous creature dodges your bullets and charges toward  you.",
                               "Then you hear the unmistakable sound of a C-20 Canister rifle.",
                               "A massive hole appears in the Hydralisk's chest, and it crumples to the ground, lifeless.",
                               "As you try to understand what happened, you hear a familiar voice:",
                               color.Color.PURPLE + "Sarah:" + color.Color.RESET + " Jim?"],
                              ["Driven by an inexplicable surge of determination, you charge the Hydralisk unarmed.",
                               "It gazes at you with bewilderment before spitting a corrosive stream of acid into your face.",
                               "Agonizing pain surges through you, and in your final moments, you hear Sarah's voice echoing, questioning your seemingly irrational decision:",
                               color.Color.PURPLE + "Sarah:" + color.Color.RESET + " Jim, you are such a noob!!!"],
                              [], [])
        marineSuit = item.Item("Suit", "CMC Powered Combat Suit", [
            "You finish putting on the combat suit. Suddenly, the radio crackles to life, and a familiar voice emerges from the speakers.",
            color.Color.PURPLE + "Sarah:" + color.Color.RESET + " This is Kerrigan, there are zergs advancing to our positions, we need immediat evac!",
            color.Color.BLUE + "Mengsk:" + color.Color.RESET + " Belay that order! We are moving out!",
            color.Color.CYAN + "James (You):" + color.Color.RESET + " *with anger* 'What! You are not just gonna leave them!'",
            color.Color.BLUE + "Mengsk:" + color.Color.RESET + " All ships prepare to move away from Tarsonis on my mark",
            color.Color.PURPLE + "Sarah:" + color.Color.RESET + " *shots and zerglings screams*... 'Uh, boys. How about that evac?'",
            color.Color.CYAN + "James (You):" + color.Color.RESET + " Damn you Arcturus, Don't do this!",
            color.Color.BLUE + "Mengsk:" + color.Color.RESET + " It's done! Helmsman, signal the fleet and take us out of orbit. Now!",
            color.Color.PURPLE + "Sarah:" + color.Color.RESET + " Commander? Jim? What the hell is going on up there? .... *radio silence*"
        ])

        

        battlecruiser = room.Room("Battle Crusier", "A standard Terran Battlecruiser orbiting planet Tarsonis.", [marineSuit], [])
        startport = room.Room("Startport", "You are inside the main startport on planet Tarsonis.", [rifle], [])
        nursery = room.Room("Nursery", "A classic terran nursery with some med kits", [stimpack], [])
        refinery = room.Room('Refinery', "A huge vespen gas refinery", [khaydarin], [zerglings])
        barracks = room.Room("Barracks", "Laying in the ground you can see several soldiers injured.", [], [marine, firebat])
        bunker = room.Room("Bunker", "A bunker with huge hole on the side probably made by a Zerg's Guardian", [], [hydralisk])

        battlecruiser.addGate(gate.Gate("down", startport, [marineSuit], []))
        startport.addGate(gate.Gate("north", barracks, [], []))
        startport.addGate(gate.Gate("west", refinery, [], []))
        barracks.addGate(gate.Gate("north", nursery, [khaydarin], []))
        barracks.addGate(gate.Gate("south", startport, [], []))
        nursery.addGate(gate.Gate("south", barracks, [], []))
        refinery.addGate(gate.Gate("east", startport, [], []))
        refinery.addGate(gate.Gate("south", bunker, [keycard], []))

        helpCommand = command.Command("help", self.helpCommand, "It will display this help menu")
        goCommand = command.Command("go", self.goCommand, "Go to a direction. e.g. 'go south'")
        getCommand = command.Command("get", self.getCommand, "You will get an object from the room. e.g. 'get key'")
        attackCommand = command.Command("attack", self.attackCommand, "You will attack an enemy unit. e.g. 'attack zerglingsassist'")
        assistCommand = command.Command("assist", self.assistCommand, "You will assist an ally unit. e.g. 'assist medic'")
        cheatCommand = command.Command("cheat", self.cheatCommand, "Don't do it Jimmy! She is a monster!")

        

        self.winningMessage = color.Color.CYAN + "Congratulations! You were able to assist Sarah! Wasn't that hard right? Right Blizzard?" + color.Color.RESET
        self.looseMessage = color.Color.CYAN + "----- GAME OVER -----" + color.Color.RESET

        self.items = [khaydarin, keycard, rifle, stimpack, marineSuit]
        self.companions = [marine, firebat]
        self.mainRoom = battlecruiser
        self.finalRoom = bunker

        self.commands = {
            goCommand.trigger: goCommand,
            getCommand.trigger: getCommand,
            attackCommand.trigger: attackCommand,
            assistCommand.trigger: assistCommand,
            helpCommand.trigger: helpCommand,
            cheatCommand.trigger: cheatCommand,
        }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Create a new instance if it doesn't exist
            cls._instance = super(StarCraft, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            # Create a new instance if it doesn't exist
            cls._instance = cls()
        return cls._instance

    @staticmethod
    def execute_command(command, gamestatus):
        # Some static method logic here
        instance = StarCraft.get_instance().finalRoom

        moveList = command.lower().split(" ", 1)
        action = moveList[0]
        target = moveList[1] if len(moveList) > 1 else ""
        
        if action in self.commands:
            instance.commands[action].method(target, gamestatus.inventory, gamestatus.currentRoom, gamestatus.companions)
        else:
            instance.message = [action + " is not a valid command"]
        return instance

    @staticmethod
    def start_game():
        instance = StarCraft.get_instance()
        result = gamestatus.GameStatus()
        result.currentRoom = instance.mainRoom.name
        return result

    ################################ COMMANDS ########################################
    ### ALL COMMANDS WILL RETURN THE MESSAGE
    def goCommand(self, param, inventory, currentRoom, companions):
        gate = currentRoom.getGateByName(param)
        if gate:
            if gate.canOpen(inventory):
                currentRoom = currentRoom.getGateByName(param).room
            else:
                return ["You can't go there..."]
        else:
            return ["That is not a valid direction, try again."]

    def getCommand(self, param, inventory, currentRoom, companions):
        print('get with param' + param)
        item = self.currentRoom.getItemByName(param)
        if item:
            self.inventory.append(item)
            self.currentRoom.items.remove(item)
            return item.message
        else:
            return ["There is nothing with that name"]
            
    
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
            self.companions = self.companions + self.init.companions
        if param.lower() == "there is no cow level":
            self.currentRoom = self.init.bunker
    ################################ COMMANDS ########################################


if __name__ == "__main__":
    obj1 = StarCraft.get_instance()
    obj2 = StarCraft.get_instance()
    obj3 = StarCraft()
    pprint.pprint(obj1 is obj3)
    #print(StarCraft.some_static_method())

    print(StarCraft.start_game().convert_to_JSON())