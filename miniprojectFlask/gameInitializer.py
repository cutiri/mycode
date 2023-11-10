import item, room, gate, command, unit, textcolor as color


class GameInitializer:
    def __init__(self) -> None:
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
            color.Color.MAGENTA + "James (You):" + color.Color.RESET + " *with anger* 'What! You are not just gonna leave them!'",
            color.Color.BLUE + "Mengsk:" + color.Color.RESET + " All ships prepare to move away from Tarsonis on my mark",
            color.Color.PURPLE + "Sarah:" + color.Color.RESET + " *shots and zerglings screams*... 'Uh, boys. How about that evac?'",
            color.Color.MAGENTA + "James (You):" + color.Color.RESET + " Damn you Arcturus, Don't do this!",
            color.Color.BLUE + "Mengsk:" + color.Color.RESET + " It's done! Helmsman, signal the fleet and take us out of orbit. Now!",
            color.Color.PURPLE + "Sarah:" + color.Color.RESET + " Commander? Jim? What the hell is going on up there? .... *radio silence*"
        ])

        battlecruiser = room.Room("Battle Crusier", "A standard Terran Battlecruiser orbiting planet Tarsonis.", [marineSuit], [], "https://legendary-digital-network-assets.s3.amazonaws.com/wp-content/uploads/2019/07/13093945/STARCRAFT_TERRAN_BATTLECRUISER_SHIP_ENV2_HEADER.png")
        startport = room.Room("Startport", "You are inside the main startport on planet Tarsonis.", [rifle], [], "https://artistmonkeys.com/wp-content/uploads/2023/10/Starcraft-Terran-versus-Zerg-4.jpg")
        nursery = room.Room("Nursery", "A classic terran nursery with some med kits", [stimpack], [], "https://cdnb.artstation.com/p/assets/images/images/035/511/313/large/daria-frealyr-kovalenko-imgonline-com-ua-compressbysize-ajuy5f3lvtoljqrq.jpg")
        refinery = room.Room('Refinery', "A huge vespen gas refinery", [khaydarin], [zerglings], "https://oyster.ignimgs.com/mediawiki/apis.ign.com/starcraft-2/1/10/Terrans.jpg")
        barracks = room.Room("Barracks", "Laying in the ground you can see several soldiers injured.", [], [marine, firebat], "https://i.redd.it/t4gq5vrx2hi31.png")
        bunker = room.Room("Bunker", "A bunker with huge hole on the side probably made by a Zerg's Guardian", [], [hydralisk], "https://www.wired.com/images_blogs/gamelife/2013/03/artwork-jim-raynor-660.jpg")

        battlecruiser.addGate(gate.Gate("down", startport, [marineSuit], []))
        startport.addGate(gate.Gate("north", barracks, [], []))
        startport.addGate(gate.Gate("west", refinery, [], []))
        barracks.addGate(gate.Gate("north", nursery, [khaydarin], []))
        barracks.addGate(gate.Gate("south", startport, [], []))
        nursery.addGate(gate.Gate("south", barracks, [], []))
        refinery.addGate(gate.Gate("east", startport, [], []))
        refinery.addGate(gate.Gate("south", bunker, [keycard], []))

        self.winningMessage = color.Color.CYAN + "Congratulations! You were able to assist Sarah! Wasn't that hard right? Right Blizzard?" + color.Color.RESET
        self.looseMessage = color.Color.CYAN + "----- GAME OVER -----" + color.Color.RESET

        self.items = [khaydarin, keycard, rifle, stimpack, marineSuit]
        self.companions = [marine, firebat]
        self.enemies = [zerglings, hydralisk]
        self.mainRoom = battlecruiser
        self.finalRoom = bunker
        self.rooms = [battlecruiser, startport, nursery, refinery, barracks, bunker]


    def winningConditionsMet(self):
        return len(self.bunker.units) == 0