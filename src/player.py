# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    ###"player" class that has player info. info includes
    ### what room they're in but what other info would be valuable?
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"Player name: {self.name} - Room: {self.room}"
    
    


