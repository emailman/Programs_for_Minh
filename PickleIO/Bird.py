class Bird:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.breed
