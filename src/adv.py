from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
        outside_input = input("Choose direction: (n,e,s,w) ")
        if outside_input == "n":
            p_1.current_room = "foyer"
        elif outside_input == "q":
            sys.exit("Qutting game")
        else:
            print("** You may only move north from here **")

    elif p_1.current_room == "foyer":
        print(room["foyer"].name)
        print(room["foyer"].description)
        foyer_input = input("Choose direction: (n,e,s,w) ")
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
        overlook_input = input("Choose direction: (n,e,s,w) ")
        if overlook_input == "s":
            p_1.current_room = "foyer"
        elif overlook_input == "q":
            sys.exit("Qutting game")
        else:
            print("** You may only move south from here **")

    elif p_1.current_room == "narrow":
        print(room["narrow"].name)
        print(room["narrow"].description)
        narrow_input = input("Choose direction: (n,e,s,w) ")
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
        treasure_input = input("Choose direction: (n,e,s,w) ")
        if treasure_input == "s":
            p_1.current_room = "narrow"
        elif treasure_input == "q":
            sys.exit("Qutting game")
        else:
            print("** You may only move south from here **")

    else:
        pass
