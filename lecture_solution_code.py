#user.py
class User:
    def __init__(self, money, cart=[]):
        self.cart = cart
        self.money = money 

    def __str__(self):
        return f"Money: ${self.money}, Cart: {self.cart}"

    def print_status(self):
        print(f"Money: ${self.money}")
        print("Cart: ")
        for p in self.cart:
            p.print_name()

    def add_to_cart(self, product):
        # check to make sure User has enough money
        if self.money >= product.price:
            # subtract price of product from money
            self.money -= product.price
            # otherwise, add the product to their cart 
            self.cart.append(product) 
        else:
            print("You don't have enough money to buy that!\n")

#product.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def __str__(self):
        return f"{self.name}: ${self.price}"

    def print_name(self):
        print(f"{self.name}")

#department.py
# should Department inherit from Store? 
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"

    def print_products(self):
        for i, p in enumerate(self.products):
            print(f"{i+1} - {p}")

#player.py
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location

    def try_direction(self, command):
        attribute = command  + '_to'

        # see if the current room has the attribute 
        # we can use a Python function called `hasattr`
        if hasattr(self.location, attribute):
            # use `getattr` to actually move to the room 
            self.location = getattr(self.location, attribute)
        else:
            print("You can't go that way!\n")

#room.py
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"
#adv.py
from room import Room
from player import Player

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
player = Player(room['outside'])
possible_directions = ['n', 's', 'e', 'w']

# Write a loop that:
while True:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    print(f"{player.location}\n")

    # when input comes in, strip off whitespace, lowercase the input, and split it 
    command = input("What would you like to do? ").strip().lower().split()[0]
    command = command[0]

    if command == 'q':
        break

    if command in possible_directions:
        # check to see if we can go in that direction 
        # if we can, go there 
        player.try_direction(command)
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    