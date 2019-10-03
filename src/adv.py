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

# start!
print(room["outside"].name)
print(room["outside"].description)

input_01 = input("Choose direction: (n,e,s,w) ")

if input_01 == "n":
    p_1.current_room = "foyer"
    print(room["foyer"].name)
    print(room["foyer"].description)
elif input_01 == "q":
    sys.exit("Qutting game")
else:
    print("You cannot move in this direction.")

input_02 = input("Choose direction: (n,e,s,w) ")

if input_02 == "n":
    p_1.current_room = "overlook"
    print(room["overlook"].name)
    print(room["overlook"].description)
elif input_02 == "e":
    p_1.current_room = "narrow"
    print(room["narrow"].name)
    print(room["narrow"].description)
elif input_02 == "q":
    sys.exit("Qutting game")
else:
    print("You cannot move in this direction.")

if p_1.current_room == "overlook":
    input_03 = input("Choose direction: (n,e,s,w) ")
    if input_03 == "s":
        p_1.current_room = "foyer"
        print(room["foyer"].name)
        print(room["foyer"].description)
    elif input_03 == "q":
        sys.exit("Qutting game")
    else:
        print("You cannot move in this direction.")
elif p_1.current_room == "narrow":
    input_04 = input("Choose direction: (n,e,s,w) ")
    if input_04 == "w":
        p_1.current_room = "foyer"
        print(room["foyer"].name)
        print(room["foyer"].description)
    elif input_04 == "n":
        p_1.current_room = "treasure"
        print(room["treasure"].name)
        print(room["treasure"].description)
    elif input_04 == "q":
        sys.exit("Qutting game")
    else:
        print("You cannot move in this direction.")

"""
Alternative attempt

# start! p_1.current_room == "outside"

for i in range(0,5):

print(room["outside"].name)
print(room["outside"].description)

input_01 = input("Choose direction: (n,e,s,w) ")

"""
