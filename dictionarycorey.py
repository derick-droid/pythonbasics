students = {
    "name ": "derick",
    "age ": 25,
    "course ": ["maths", "programming"]

}
print(students["name "])
print(students["age "])
print(students["course "])
print()
# accessing values which are not in the dictionary without getting an error

print(students.get("phone", "not found"))

# adding values into the dictionary
print()

students["name "] = "dave"

print(students.get("name ", "not found"))
print()

# updating the dictionary we use the the update function
students.update({"name ":"javan", "phone ":555})
print(students)
# deleting data from  a dictionary we use the del funtion
print()
del students["age "]
print(students)

print()
# we can also use the pop function

age = students.pop("name ")
print(students)
print(age)
# looping over a dictionary

for key, value in students.items():
    print(key, value)