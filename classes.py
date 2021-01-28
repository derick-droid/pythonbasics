class Point(): # defining a class
    def move(self):
        print("move the point ")

    def draw(self):
        print("drawing the point ")


movement = Point()
movement.x = 12 # attribute objects
movement.z = 23
movement.draw()
movement.move()
print(movement.x)
print(movement.z)