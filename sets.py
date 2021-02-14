# python sets rejects duplicates
# sets is collection of data
a = set()
print(a)
a.add(45)
print(a)
a.add(45) # sets rejects duplication
print(a)

# iterating over a set

for elements in a:
    print(elements)

# using sets to remove duplicate in alist
numbers = [1, 2, 3, 4, 4, 1, 44, 22, 22, 1,]
new_set = set()
for elements in numbers:
    new_set.add(elements)
print(new_set)

# adding different value types in python

c= set()
c.add("microsoft")
c.add("apple")
c.add(23)
print(c)  # sets do not maintain the order of the elements added into it

# adding the unique values in a list
numbers1 = [1, 2, 1, 4, 3, 4, 5, 5, 6, 6]
uniques = set()
for items in numbers1:
    uniques.add(items)
for items in uniques:
    result = items + items
print(result)
