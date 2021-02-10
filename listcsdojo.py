
a = [ 1, 2, 4, 6, 7, 8 ]

a.append(34)
print(a)

# adding a list into yhe list

a.append([1, 4, 5, 6, ])
print(a)
# swapping within the list

b = ["banana", "apple", "microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

# using another method
b[1], b[2] = b[2], b[1]
print(b)