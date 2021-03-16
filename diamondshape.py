num = int(input("enter row: "))
num1 = int(input("enter row1: "))

# upright pyramid code
for i in range(0, num):
    for j in range(0, num-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()
# combining the codes to form a diamond shape


# inverse pyramid code
for i in range(num, 0, -1):
    for j in range(0, num1-i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()