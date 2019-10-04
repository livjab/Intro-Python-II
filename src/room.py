# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item_list=[]):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.n_to = []
        self.e_to = []
        self.s_to = []
        self.e_to = []

    def add_item(self, item):
        """Adds an item to this room. This may happen when a player drops an
        item in this room."""
        self.item_list.append(item)

    def remove_item(self, item):
        """Removes item from room. This may happen when a player picks up an
        item and leaves the room."""
        self.item_list.remove(item)
