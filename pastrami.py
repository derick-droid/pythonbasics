# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
# in finished_sandwiches .

sandwich_orders = ["tuna", "Classic club", "Ham and Cheese", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []
while sandwich_orders:
    if "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami") # removing pastrami from the list using while loop
    making_sandwiches = sandwich_orders.pop()
    print(f"I made your {making_sandwiches}")
    finished_sandwiches.append(making_sandwiches)

print()
for sandwich in finished_sandwiches:
    print(f"I made {sandwich} very delicious")