# METHODS WE CAN BE USED TO OPERATE ON OUR LISTS

numbers = [5, 2, 6, 3, 2, 4, 8]
numbers.append(10)  # THE APPEND FUNCTION IS USED TO ADD ITEMS IN THE LIST
print(numbers)
numbers.insert(0,23)  # THE INSERT METHOD IS USED TO ADD ITEMS IN THE LIST AT ANY INDEX
print(numbers)
numbers.remove(5)  # THE REMOVE FUNCTION IS USED TO REMOVE AN ITEM FROM THE LIST
print(numbers)
# numbers.clear() # THE CLEAR METHOD IS USED TO CLEAR ALL THE ITEMS FROM THE LIST
print(numbers)
numbers.pop()  # THE POP METHOD IS USED TO REMOVE THE LAST ITEM IN THE LIST
print(numbers)
print(numbers.index(23))  # THE INDEX METHOD IS USED TO CHECK THE INDEX OF A VALUE IN A LIST
number = numbers.copy()  # THE COPY METHOD IS USED TO COPY A LIST TO FORM A SIMILAR LIST
print(number)
print(50 in number)  # THE IN OPERATOR CAN BE USED TO CHECK EXISTANCE OF AN ITEM IN A LIST
print(numbers.count(2) )  #  THE COUNT METHOD CAN BE USED TO CHECK HOW MANY TIMES DOES AN ITEM APPEARS IN THE LIST
numbers.sort()  # THE SORT METHOD IS USED TO ARRANGE THE FIGURES IN THE LIST IN ASCENDING ORDER
print(numbers)
numbers.reverse()  # THE REVERSE METHOD IS USED TO REVERSE THE ARRANGEMENT VALUES IN A LIST
print(numbers)

#  LIST METHOD EXERCISE
#  TO REMOVE DUPLICATE IN A LIST

numbers2 = [5, 2, 2, 5, 6, 7, 8, 9]
new_list = []
for number in numbers2:
    if number not in new_list:
        new_list.append(number)
print(new_list)