# looping over a list of an item
magicians = ["alice", "nana", "caroh"]
for magician in magicians:
    print(f"{magician.title()}  you did a good work")
    print("I cannot wait to see your next trick \n")

# exercise

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!


pizza_name = [" Neapolitan Pizza", "chicago pizza", "Greek pizza"]
for pizza in pizza_name:
    print(f"i like {pizza} , it is my favourite")

print("I really like pizza")

# exercise 2
#
# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# 60     Chapter 4
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

animals_name = ["dog", "cat", "horse"]
for animals in animals_name:
    print(f"{animals} can make a good pet")
print("I like pets")
