# creating a class for a dog
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"the dog {self.name} is now sitting")

    def rollover(self):
        print(f"{self.name} is rolling")

# creating instance of a class


my_dog = Dog("rex", 23)
print(f"my dog name is {my_dog.name}")
print(f"my dog is {my_dog.age} old")
