# doubling elements in a list
a = [1, 34, 6, 54, 344, 4555, 4]
b = []
for elements in a:
    multiple = elements * 2
    b.append(multiple)
print(b)

# list comprehension
b = [elements * 2 for elements in a]
print(b)

