# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

numbers = [1, 3, 2, 4, 5, 6, 7, 8, 9]
slice1 = numbers[:3]
slice2 = numbers[4:]
slice3 = numbers[-3:]
print(f"The first three items in the list are:{slice1}")
print(f"The items from the middle of the list are:{slice2}")
print(f"The last three items in the list are:{slice3}")
print()
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas .
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas .
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.
print()

pizzas = ["chicago pizza", "new york_style pizza", "greek pizza", "neapolitans pizza"]
friends_pizza = pizzas[:]
pizzas.append("sicilian pizza")
friends_pizza.append("Detroit pizza")
print(f"my favourite pizzas are:{pizzas}")
print()
print(f"my friend favourite pizzas are:{friends_pizza}")
print()
print("my favourite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print()
print("my favourite pizzas are: ")
for items in friends_pizza:
    print(items)
    print()
#
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

food_stuff = ["cake", "rice", "meat", "ice cream", "banana"]
food = ["goat meat", "pilau", "egg stew", "fried", "meat stew"]

for foodz in food_stuff:
    print(foodz)
print()

for itemz in food:
    print(itemz)