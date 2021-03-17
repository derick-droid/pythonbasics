for row in range(4):
    for col in range(8):
        if (col == 0 or col == 7 ) or (row == 0 or row == 3):
            print("*", end="   ")
        else:
            print(end="    ")
    print()