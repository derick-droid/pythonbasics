# returning dictionary in functionn
def user_dictionary (first_name, last_name):
    full = {
       "first_name"  : first_name,
        "last_name" : last_name
    }
    return full 
    
musician = user_dictionary("ford", "dancan")
print(musician)
# using optinal values in dictionary

def dev_person(occupation, age, home_town = ""):
    if home_town:
         person = {
        "occupation" : occupation,
        "age" : age,
        "home_town" : home_town
    }
         return person
    else:
        person = {
            "occupation" : occupation,
            "age" : age
        }
    return person

user = dev_person("software developer", "23", "Migori")
print(user)

    