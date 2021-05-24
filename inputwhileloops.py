#  prompt helps when one wants to display along message
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(name)
print()

# use int() input
#  determining the appropriaate height to ride a bicycle

height = int(input("what is your height: "))
if height >= 72:
    print("yo are qualified to ride")
else:
    print("Not qualified to ride ")

# module operator can be used to to find even numbers  while demonstrating the basics of user input

number = int(input("enter number: "))
if number % 2 == 0:
    print("it is even number")
else:
    print("it is odd number ")




