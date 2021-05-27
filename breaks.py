# using breaks in while loops
prompt = "\n enter your own message , we wiil keep your message secret!"
prompt += "\n enter message:"

while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    else:
        print(message)
