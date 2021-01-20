for x in range (5):
    for y in range (4):
        print(f"{x}, {y} ")

#EXERCISE OF NESTED LOOPS

numbers = [5, 2, 5, 2, 2 ]
for number in numbers: # BUT NO NESTED LOOPS USED
    print("*" * number)

# USING NESTED LOOPS

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ""
    x_counts = output
    for item in x_counts:
        print("*" * item)