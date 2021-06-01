# using while loop with the dictionary
# filling a dictionary with user input

responses = {}
# prompting user to enter name and mountain to climb
poll_active = True
while poll_active:
    name = input("enter your name: ")
    mountain = input("enter mountain: ")
    responses[name] = mountain
    request = input("would like somebody else to come (yes/no: ")
    if request.lower() == "no":
        poll_active = False
print("this are the result: ")
for name, mountain in responses.items():
    print(f"{name} likes {mountain}")
