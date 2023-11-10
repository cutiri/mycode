import json, room, customJSONencoder

class GameStatus:
    def __init__(self):
        self.inventory = []
        self.companions = []
        self.currentRoom = None
        self.message = []
        self.hp = 100
        self.image = ""
    
    def convert_to_dict(obj):
        if isinstance(obj, GameStatus):
            return {'name': obj.name, 'age': obj.age}
    
    def convert_to_JSON(self):
        return json.dumps(self, cls=customJSONencoder.CustomJSONEncoder, indent = 2)
    





if __name__ == "__main__":
    gs = GameStatus()
    gs.inventory = ["sword", "rifle"]
    gs.message = ["Hello", "World"]
    gs.currentRoom = room.Room("Room name", "Room Description", [], [])
    json_data = json.dumps(gs, cls=CustomJSONEncoder, indent=2)
    print(json_data)