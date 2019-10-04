from item import Item
from room import Room
from player import Player
import sys


# Declare all the items

item = {
    'egg':  Item("Egg",
                 """A small, round, white egg, possibly from a chicken. By the
                 smell, it seems to be hardboiled."""),

    'sock': Item("Sock",
                 """An old, smelly, gym sock. While this sock was once white, it
                 has now faded into a dingy gray color."""),

    'can':  Item("Can",
                 "A rusted beer can, the label of which you can no longer read."),

    'bag':  Item("Bag",
                 """A crumpled plastic grocery bag, with yellow coloring that
                 may have once been a smiley face."""),

    'bic':  Item("Bic",
                 """A Bic lighter, empty of lighter fuel, and spark wheel rusted
                 to the point of complete inefficacy"""),
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["bag", "can"]),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run
north and east.""",
                     ["egg"]),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the
darkness. Ahead to the north, a light flickers in the distance, but there
is no way across the chasm.""",
                     ["bic", "can", "bag"]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The
smell of gold permeates the air.""",
                     ["sock", "egg"]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it
has already been completely emptied by earlier adventurers. The only exit is
to the south.""",
                     ["bic", "sock"])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

p_1 = Player(name="Liv")
#My player class instantiates every player to start outside.

# start! p_1.current_room == "outside"

for i in range(0,1000):

    if p_1.current_room == "outside":
        print(room["outside"].name)
        print(room["outside"].description)
        print(f"In this room are the following items: ", room["outside"].item_list)
        outside_input = input("Choose direction (n,e,s,w) or get/drop item: ")

        if len(outside_input.split()) > 1:
            if outside_input.split()[0] == "get":
                p_1.add_item(outside_input.split()[1])
                room["outside"].remove_item(outside_input.split()[1])
                print("You have picked up item. You have the following items: ")
                print(p_1.item_list)
            elif outside_input.split()[0] == "drop":
                p_1.remove_item(outside_input.split()[1])
                room["outside"].add_item(outside_input.split()[1])
                print("You have dropped item. You have the following items: ")
                print(p_1.item_list)
            else:
                print("Not a valid entry")

        else:
            if outside_input == "n":
                p_1.current_room = "foyer"
            elif outside_input == "q":
                sys.exit("Qutting game")
            else:
                print("** You may only move north from here **")

    elif p_1.current_room == "foyer":
        print(room["foyer"].name)
        print(room["foyer"].description)
        print(f"In this room are the following items: ", room["foyer"].item_list)
        foyer_input = input("Choose direction: (n,e,s,w) ")

        if len(foyer_input.split()) > 1:
            if foyer_input.split()[0] == "get":
                p_1.add_item(foyer_input.split()[1])
                room["foyer"].remove_item(foyer_input.split()[1])
                print("You have picked up item. You have the following items: ")
                print(p_1.item_list)
            elif foyer_input.split()[0] == "drop":
                p_1.remove_item(foyer_input.split()[1])
                room["foyer"].add_item(foyer_input.split()[1])
                print("You have dropped item. You have the following items: ")
                print(p_1.item_list)
            else:
                print("Not a valid entry")

        else:
            if foyer_input == "n":
                p_1.current_room = "overlook"
            elif foyer_input == "e":
                p_1.current_room = "narrow"
            elif foyer_input == "s":
                p_1.current_room = "outside"
            elif foyer_input == "q":
                sys.exit("Qutting game")
            else:
                print("** There is nothing to the west **")

    elif p_1.current_room == "overlook":
        print(room["overlook"].name)
        print(room["overlook"].description)
        print(f"In this room are the following items: ", room["overlook"].item_list)
        overlook_input = input("Choose direction: (n,e,s,w) ")

        if len(overlook_input.split()) > 1:
            if overlook_input.split()[0] == "get":
                p_1.add_item(overlook_input.split()[1])
                room["overlook"].remove_item(overlook_input.split()[1])
                print("You have picked up item. You have the following items: ")
                print(p_1.item_list)
            elif overlook_input.split()[0] == "drop":
                p_1.remove_item(overlook_input.split()[1])
                room["overlook"].add_item(overlook_input.split()[1])
                print("You have dropped item. You have the following items: ")
                print(p_1.item_list)
            else:
                print("Not a valid entry")

        else:
            if overlook_input == "s":
                p_1.current_room = "foyer"
            elif overlook_input == "q":
                sys.exit("Qutting game")
            else:
                print("** You may only move south from here **")

    elif p_1.current_room == "narrow":
        print(room["narrow"].name)
        print(room["narrow"].description)
        print(f"In this room are the following items: ", room["narrow"].item_list)
        narrow_input = input("Choose direction: (n,e,s,w) ")

        if len(narrow_input.split()) > 1:
            if narrow_input.split()[0] == "get":
                p_1.add_item(narrow_input.split()[1])
                room["narrow"].remove_item(narrow_input.split()[1])
                print("You have picked up item. You have the following items: ")
                print(p_1.item_list)
            elif narrow_input.split()[0] == "drop":
                p_1.remove_item(narrow_input.split()[1])
                room["narrow"].add_item(narrow_input.split()[1])
                print("You have dropped item. You have the following items: ")
                print(p_1.item_list)
            else:
                print("Not a valid entry")

        else:
            if narrow_input == "w":
                p_1.current_room = "foyer"
            elif narrow_input == "n":
                p_1.current_room = "treasure"
            elif narrow_input == "q":
                sys.exit("Qutting game")
            else:
                print("** You may only move west or north from here **")

    elif p_1.current_room == "treasure":
        print(room["treasure"].name)
        print(room["treasure"].description)
        print(f"In this room are the following items: ", room["treasure"].item_list)
        treasure_input = input("Choose direction: (n,e,s,w) ")

        if len(treasure_input.split()) > 1:
            if treasure_input.split()[0] == "get":
                p_1.add_item(treasure_input.split()[1])
                room["treasure"].remove_item(treasure_input.split()[1])
                print("You have picked up item. You have the following items: ")
                print(p_1.item_list)
            elif treasure_input.split()[0] == "drop":
                p_1.remove_item(treasure_input.split()[1])
                room["treasure"].add_item(treasure_input.split()[1])
                print("You have dropped item. You have the following items: ")
                print(p_1.item_list)
            else:
                print("Not a valid entry")

        else:
            if treasure_input == "s":
                p_1.current_room = "narrow"
            elif treasure_input == "q":
                sys.exit("Qutting game")
            else:
                print("** You may only move south from here **")

    else:
        pass
