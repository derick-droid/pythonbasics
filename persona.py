class Robots:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_yourself(self):
        print("my name is  " + self.name )
        print("I am  " + self.color )
        print("I weigh " + self.weight)


r1 = Robots("Tom", "blue", "34kg")
r2 = Robots("Derrick", "yellow", "50kgs")
r1.introduce_yourself()
print("              ")
r2.introduce_yourself()