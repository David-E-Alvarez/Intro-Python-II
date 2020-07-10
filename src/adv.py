from room import Room
from player import Player
# Declare all the rooms

room = {# "room" is a dictionary. What do I know about Python dictionaries?
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
player1 = Player("Jack", room["outside"])

# Write a loop that:
#
while True:#what ends this?
    # * [x]Prints the current room name
    print(f"current room: {player1.room.name}\n")

    # * [x]Prints the current description (the textwrap module might be useful here).
    print(f"room description: {player1.room.description}\n")

    # * [x]Waits for user input and decides what to do.
    user_input = input("press n for north, e for east, s for south, w for west, or q to quit please : ")
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
        #why wouldn't a movement be alowed? how wouldn't it be allowed?

    # if someone presses 'n' go to foyer(player always begins outside )
    # if not let user know they cant go in desired direction
    if user_input == 'n': # can player go in the direction user wants to?
        if player1.room.n_to is not None:
            player1.room = player1.room.n_to
        else:
            print('cant go in that direction')
    if user_input == 'e':
        if player1.room.e_to is not None:
            player1.room = player1.room.e_to
        else:
            print('cant go in that direction')
    if user_input == 's':
        if player1.room.s_to is not None:
            player1.room = player1.room.s_to
        else:
            print('cant go in that direction')
    if user_input == 'w':
        if player1.room.w_to is not None:
            player1.room = player1.room.w_to
        else:
            print('cant go in that direction')

    
    # [x]If the user enters "q", quit the game.
    if user_input == 'q':
        break
