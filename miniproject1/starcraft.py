import question

def trivia_pool():
    return [
        question.Question("If you were being attacked by Siege Tanks, what units would be best to send in to counter the threat that Siege Tanks could not harm?",
                           [ "Wraiths", "Hydralisks", "Scourge", "Dragoons"], [ 0 ]),
        question.Question("If a unit is able to see cloaked units, it will be displayed in the information window. What word will appear?", 
                          [ "Detector", "Scanner", "Sensor", "It depends on which race you play as"], [ 0 ]),
        question.Question("The Protoss get a rather deadly unit called a Carrier. The Carrier can create and house Interceptors, small, agile ships that can quickly attack enemies without being hit too hard. What happens to Interceptors when their Carrier is destroyed?",
                           [ "They become wild and attack everything", "They kamakaze the nearest enemy unit", "They detonate", "They fly to another Carrier with open slots"], [ 2 ]),
        question.Question("The Zerg Guardian can only attack one kind of unit. Which is it?",
                           [ "Air", "Ground", "Cloaked", "Seaworthy"], [ 1 ]),
    ]


