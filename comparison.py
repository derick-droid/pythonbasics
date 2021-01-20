# >,>, >=,<=,==, !=
temperature = 30
if temperature >= 35:
    print("it is hot day ")
else:
    print("it is a lovely day")
#COMPARISON OPERATOR EXERSICE

name = input("name:  ")
if len(name) < 3: # LEN FUNCTION COUNT NUMBER OF CHARACTERS ENTERED BY THE USER
    print("characters must be at least 3")
elif len(name) > 10:
    print("character must be at most 10")
else:
    print("lovely name")