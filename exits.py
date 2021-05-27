# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

  # active
active = True
while active:
    message = int(input("enter age: "))
    if message == 0:
        active = False
    elif message < 3:
        print("your ticket is free")

    elif message <= 12:
        print("your ticket is $10")

    else:
        print("your ticket is $15")

print()

   # break
while True:
    message = input("enter age: ")
    if message == "quit":
        break
    else:
        print(f"your {message} is")

