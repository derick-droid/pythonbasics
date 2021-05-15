alien_0 = {
    "colour" : "green",
    "points" : 5
}
print(alien_0["colour"])
print(alien_0["points"])
new_alien = alien_0["points"]
print(f"your new point is {new_alien} that is very good")
print()

# adding values in dictionary
print(alien_0)
alien_0["x_coordinate"] = 0
alien_0["y_coordinate"] = 25
alien_0["size"] = "big head"
print(alien_0)

print()
# starting with an empty dictionary and adding values to it

students = {}
students["name"] = "derrick kibaso"
students["registration number"] = "ICT-G-4-0579-18"
print(students)

# Modifying Values in a Dictionary
print()

vampire = {
    "color": "green",
           }
print(vampire["color"])
vampire["color"] = "yellow"
print(vampire["color"])

# detailed example:
# to determine the speed of the vampire across its points

vampire["x_coordinate"] = 4
vampire["y_coordinate"] = 5
vampire["speed"] = "high speed"

print(vampire)

if vampire["speed"] == "medium":
    x_increment = 1

elif vampire["speed"] == "high speed":
    x_increment = 4
elif vampire["spedd"] == "extra speed":
    x_increment  = 5

new_point = vampire["x_coordinate"] + x_increment
print(f" new point:  {new_point} ")
print()

# Removing Key-Value Pairs
print(vampire)

del vampire["y_coordinate"] # deleting key_value from dictionary

print(vampire)
print()

# A Dictionary of Similar Objects
favourite_languages = {
    "derrick" : "java",
    "sarah" : "c",
    "don" : "pascal"

}
print("sarah's favourite language is " + favourite_languages["sarah"].title() + ".")
print(f"sarah is {favourite_languages["sarah"] } ")