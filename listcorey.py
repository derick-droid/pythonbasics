courses = ["history", "geography", "maths", "compsci"]

# using for loop to access both index and items in the list

for index, course in enumerate(courses):  # we use the enumerate function
    print(index, course)
print()

# if we want to start from index 1 we add start statement

for index, course in enumerate(courses, start=1):
    print(index, course)
print()
# we can turn list into a string

course_str = "-".join(courses)
print(course_str)
print()


# return a string into list

# create a new variable
new_list = course_str.split("-")
print(new_list)
