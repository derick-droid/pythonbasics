prompt = "\nenter your message here please:"
prompt += "\n enter message:"
# using flags in while loops
active = True 
while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        print(message)


