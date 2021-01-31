import random
value = random.random()  # random numbers between 1 and 0
print(value)

for i in range(3):
    print(random.randint(20,56))  # this gives random numbers between numbers specified

members = ["derick", "john", "conf"]
leader = random.choice(members)
print(leader)

# exercise choosing random numbers
# dice game


class Dice:

    def roll(self):

        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())
