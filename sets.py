# sets sorting of data is not considered
# sets don't allow any duplication of data

# sets can be used to check if two sets share common data this can be by using the intersection function

course = {"maths", "Compsci", "chemistry", "history", "statistics", "Compsci"}
print(course)

print()
art_course = {"maths", "Compsci", "geography", "physics", "biology", "music"}
bus_course = {"maths", "computer ", "java ", "googles", "modes", "dental"}
print(course.intersection(art_course, bus_course))

print()
# want show not common data in the available sets we use the "difference" function

print(course.difference(art_course, bus_course))
# combine thes sets together we use the union function

print()

print(course.union(art_course, bus_course))

# creating empty set we the set function

empty_set = set()


