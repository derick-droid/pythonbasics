class Mammal:
    def walk(self):
        print('walking')

class Dog(Mammal):

    def bark(self):
        print("barking")

class Cat(Mammal):
    def meaw(self):
        print("meaw")



dog = Dog
dog.bark(Mammal)
dog.walk(Mammal)
cat = Cat
cat.walk(Mammal)
cat.meaw(Mammal)