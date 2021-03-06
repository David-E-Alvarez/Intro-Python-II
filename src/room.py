# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    ### "room" with "name" and "description" attributes
    def __init__(self,name,description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}-{self.description}-{self.items}"
    