import room, gate, command, unit, item

def test(val1, val2):
    print("Pass" if val1 == val2 else "Fail")

khaydarin = item.Item("Khaydarin", "A piece of Khaydarin Crystal, it's blue and shinny", "")
keycard = item.Item("Key Card", "A bloody key card, a name is still visible, it belonged to Edmund Duke", "")
rifle = item.Item("rifle", "A C-14 Impaler gauss rifle, is the standard marine rifle", "")
stimpack = item.Item("stimpack", "A brand new stimpack never used", "")

firebat = unit.Unit("Firebat", True, None, None, "", "", [], [stimpack])
marine = unit.Unit("Marine", True, None, None, "", "", [], [stimpack])
zerglings = unit.Unit("Zerglings", False, firebat, None, "With a swift, precise sweep of his flamethrower, your fellow Firebat incinerates the charging Zerglings, turning them into ashes in the blink of an eye. Then you see a keycard one of them was chewing.", 
                        "You start shooting at the zerglings but they are too many and soon overwealm you, one of them is able to reach you and stab you in the chest, you fall to the ground and soon loose conciousness.",
                        [keycard], [])
hydralisk = unit.Unit("Hydralisk", False, None, rifle, "As you aim your C-14 Impaler at the Hydralisk and open fire, the hideous creature deftly dodges your bullets and charges toward you. In the nick of time, you hear the unmistakable sound of a C-20 Canister rifle. A massive hole appears in the Hydralisk's chest, and it crumples to the ground, lifeless.",
                        "Driven by an inexplicable surge of determination, you charge the Hydralisk unarmed. It gazes at you with bewilderment before spitting a corrosive stream of acid into your face. Agonizing pain surges through you, and in your final moments, you hear Sarah's voice echoing, questioning your seemingly irrational decision.",
                        [], []) 

khaydarin = item.Item("Khaydarin", "A piece of Khaydarin Crystal, it's blue and shinny", "")
keycard = item.Item("Key Card", "A bloody key card, a name is still visible, it belonged to Edmund Duke", "")
rifle = item.Item("rifle", "A C-14 Impaler gauss rifle, is the standard marine rifle", "")
marineSuit = item.Item("suit", "CMC Powered Combat Suit", [
    "You finish putting on the combat suit. Suddenly, the radio crackles to life, and a familiar voice emerges from the speakers.",
    "Sarah: This is Kerrigan, there are zergs advancing to our positions, we need immediat evac!",
    "Mengsk: Belay that order! We are moving out!",
    "You take the intercom and angrily say: 'What! You are not just gonna leave them!'",
    "Mengsk: All ships prepare to move away from Tarsonis on my mark",
    "Sarah: *shots and zerglings screams*... 'Uh, boys. How about that evac?'",
    "You say: Damn you Arcturus, Don't do this!",
    "Mengsk: It's done! Helmsman, signal the fleet and take us out of orbit. Now!",
    "Sarah: Commander? Jim? What the hell is going on up there? .... *radio silence*"
])

battlecruiser = room.Room("Battle Crusier", "A standard terran Battle Crusier", [marineSuit], [])
startport = room.Room("Startport", "You are inside the main startport on planet Tarsonis.", [rifle], [])
nursery = room.Room("Nursery", "A classic terran nursery with some med kits", [stimpack], [])
refinery = room.Room('Refinery', "A huge vespen gas refinery", [], [zerglings])
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


##### TEST AREA ####

#Unit:
test(firebat.assist([keycard]), False)
test(firebat.assist([]), False)
test(firebat.assist([stimpack]), True)
test(firebat.assist([keycard, stimpack]), True)
test(marine.assist([keycard, rifle, stimpack]), True)
test(marine.assist([rifle]), False)
test(marine.assist([stimpack]), True)