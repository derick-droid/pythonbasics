# Looping Through All Key-Value Pairs
user_0 = {
    "user_name" : "arridez",
    "first_name" : "derrick",
    "last_name" : "beatrice",

}
for key, value in user_0.items():
    print("key: \n" + key)
    print("value:  \n" + value)

    print()

# Looping Through All the Keys in a Dictionary

favorite_languages = {
    "seth" : "python",
    "don" : "ruby",
    "jack" : "php"
}
friends = ["seth", "jack"]
for name in favorite_languages.keys():
    print(name)
print()
# checking and comparing other list and then give a message

for name, language in favorite_languages.items():
    if "dave" not in favorite_languages:
        print("please Dave register your name")

    if  name in friends:
        print(f" Hi {name} your friends favorite language is {language}")

print()

# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(f" Hi programmers {name}")
print()

# Looping Through All Values in a Dictionary
for value in favorite_languages.values():
    print(value)

    print()
# using set to remove duplicate sin the dictionary

for value in set(favorite_languages.values()):
    print(value)





