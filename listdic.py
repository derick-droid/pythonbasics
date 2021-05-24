# stores information of pizza being ordered
pizza = {
    "crust" : "thirst",
    "topping" : ["mushroom", "extra cheese"]
}

# summary of  the order
print("Your ordered pizza " + pizza["crust"] + "-crust pizza has the following toppings: ")
for item in pizza["topping"]:
    print(item)

# more examples

students = {
    "derrick" : ["python", "Java", "c++", "javascript"],
    "Kibaso" : ["HTML", "css", "javascript"]
}
for name, languages in students.items():
    print(name.title() + "'s favourite language is: " )
    for language in languages: # because it is a list for loop over through to print each element
        print(language)