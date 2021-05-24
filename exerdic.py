# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets . Next, loop through your list
# and as you do print everything you know about each print it

rex = {
    "name" : "rex",
    "kind": "dog",
    "owner's name" : "joe"
}

pop = {
    "name" :"pop",
    "kind" : "pig",
    "owner's name": "vincent"
}
dough = {
    "name": "dough",
    "kind" : "cat",
    "owner's name" : "pamna"
}

pets = [rex, pop, dough ]

for item in pets:
    print(item)

print()

# 6-9. Favorite Places: Make a dictionary called favorite_places . Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.


favorite_places = {
    "derrick": {
        "nairobi", "mombasa", "kisumu"
    },
    "dennis":{
        "denmark", "thika", "roman"
    },
    "john": {
        "zambia", "kajiado", "suna"
    }

}
for name, places in favorite_places.items(): # looping through the dictionary and printing only the name variable
    print(f"{name} 's favorite places are :")
    for place in places: # looping through the places variable to come up with each value in the variable
        print(f"-{place}")
print()
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_number = {
    "derrick" : [1, 2, 3],
    "don" : [3, 5, 7],
    "jazzy" : [7, 8, 9]
}

for name, fav_number in favorite_number.items():
    print(f"{name} favorite numbers are: ")
    for number in fav_number:
        print(f"-{number}")
# 6-11. Cities: Make a dictionary called cities . Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country , population , and fact . Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    "Nairobi" : {
        "population" : "1400000",
        "country" : "kenya",
        "facts" : "largest city in East Africa"
    },
    "Dar-es-salaam" : {
        "population" : "5000000",
        "country" : "tanzania",
        "facts" : "largest city in Tanzania"
    },
    "Kampala" : {
        "population" : "1000000",
        "country" : "Uganda",
        "facts" : "The largest city in Uganda"
    }
}
for city, information  in cities.items():
    print(f"{city}:")
    for fact,facts in information.items():
        print(f"-{fact}: {facts}")
