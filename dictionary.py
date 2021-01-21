# DICTIONARY ARE USED TO STORE KEY INFORMATION

customer = {

    "name ": "derrick kibs",
    "age " : 30,
    "phone " : 1234

}
print(customer["name "])
print(customer["age "])
print(customer["phone "])
print(customer.get("birthdate"))  # TO KNOW IF A KEY VALUE EXIST IN A DICTIONARY
print(customer.get("birth date ", "jan 12 2006")) # ADDING A KEY WHICH DOES NOT EXIST IN THE DICTIONARY

#  DICTIONARY EXERCISE
#  IF I TYPE INTEGERS I GET OUTPUT IN WORDS

number = input("enter numbers: ")
numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
for items in number:
    if items == 1:
        print("one")



