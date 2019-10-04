# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room='outside'):
        self.name = name
        self.current_room = current_room
        self.item_list = []

    def add_item(self, item):
        """Adds an item to this player. This occurs when a player picks up an
        item from a room."""
        self.item_list.append(item)

    def remove_item(self, item):
        """Removes item from room. This may happen when a player drops an
        item in the room and leaves."""
        self.item_list.remove(item)
