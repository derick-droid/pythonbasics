# Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name , last_name , age , and city . Print each
# piece of information stored in your dictionary.

person = {
    "first_name" : "derrick",
    "last_name" : "okinda",
    "age" : 43,
    "city" : "Nairobi"

}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

print()

# Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number.

favorite_number = {
    "derrick": 1,
    "enock": 2,
    "elisha": 3,
    "charles": 4,
    "denno": 5
}
print(" derrick's favorite number is " + str(favorite_number["derrick"]) + ".")
print("enock's favorite number is " + str(favorite_number["enock"]) + ".")
print("elisha's favorite number is " + str(favorite_number["elisha"]) + ".")
print("charles' favorite number is " + str(favorite_number["charles"]) + ".")
print("denno's favorite number is " + str(favorite_number["denno"]) + ".")

print()

# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character ( \n ) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    "pep" : "python enhancemnt proposal",
    "programming" : "writing sets of instruction ",
    "coding" : "writing codes",

}

print("pep \n" + glossary["pep"])
print("programming \n" + glossary["programming"])
print("coding \n" + glossary["coding"])


