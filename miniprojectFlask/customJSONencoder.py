import gamestatus, room, item, gate, json, unit

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, gamestatus.GameStatus):
            return {'inventory': obj.inventory, 'companions': obj.companions, 'message': obj.message, 'currentRoom': obj.currentRoom}
        if isinstance(obj, room.Room):
            return { 'name': obj.name, 'description': obj.description, 'units': obj.units, 'items': obj.items, 'gates':obj.gates }
        if isinstance(obj, item.Item):
            return { 'name': obj.name }
        if isinstance(obj, unit.Unit):
            return { 'name': obj.name }
        if isinstance(obj, gate.Gate):
            return { 'direction': obj.direction }
        return super().default(obj)