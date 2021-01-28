# constructor is the function being called at the time of creating objects

class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 37)
print(point.y)
print(point.x)

# EXERCISE

class Person:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f" {self.first_name}is talking ")
        print(f"{self.last_name} is taking")


name1 = Person("derrick", "okinda")
print(name1.first_name)
name1.talk()
print(name1.last_name)
name1.talk()