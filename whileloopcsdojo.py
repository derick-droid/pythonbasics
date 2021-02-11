# calculating total using while loops
total = 0
j = 1
while j < 5:
    total += j
    j += 1
print(total)

# adding elements in a list using while loop

numbers = [5, 4, 3, 2, 1, -1, -2, -3, ]
total2 = 0
i = 0
while i < len(numbers) and numbers[1] > 0:
    total2 += i
    i += 1
print(total2)

# adding elements in a list using while loop and breaks

numbers1 = [7, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7]
result = 0
 # i = 0
for items in numbers1:
    if items < 0:
        print(items)
        result += items
print(result)

total3 = 0
i = -1
while numbers1[i] < 0:
    total3 += i
    i -= 1
    print(numbers1[i])
    print(i)
print(total3)


