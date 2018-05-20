# Shared import
from guizero import *

# Global list
bodies = []

# Global widget
app = App(title="Welcome to the Morgue",
          height=300, width=300)


# Global class
class Corpse:
    count = 0

    def __init__(self, gender):
        Corpse.count += 1
        self.index = Corpse.count
        self.gender = gender
        if gender == "M":
            self.name = "John Doe"
        else:
            self.name = "Jane Doe"

    def __str__(self):
        return str(self.index) + " : " + self.gender + " : " +\
               self.name
