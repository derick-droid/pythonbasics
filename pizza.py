# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
# exercise on while loops basics
prompt = "\n enter a serie of pizza toppings "
prompt += "\n enter toppings: "
while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    else:
        print(f"we will add {message} to your pizza")