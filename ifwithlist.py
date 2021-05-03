# if statement with a list

pizzare = ["mushroom", "chocolate", "carlifornia", "newyork"]

for pizza in pizzare:
    if pizza == "newyork":
        print("still not available")
    else:
        print(f"{pizza} is being added please just wait a moment")
print()
# Checking That a List Is Not Empty

topping_list = []
if topping_list:
    for requset in topping_list:
        print(f"{requset} is being added please be patient")

else:
    print("are sure you want plain pizza")

print()
# Using Multiple Lists

vailable_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requset_topping = ["french fry","chicken baker", "chips soda", "olives"]

for piza in requset_topping:
    if piza in vailable_toppings:
        print(f"{piza} is being added please be patient")
    else:
        print(f"{piza} is not available")