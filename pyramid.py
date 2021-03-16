num = int(input("enter number of rows : "))
for i in range(0, num):
    for j in range(i, num-1):
        print(end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()