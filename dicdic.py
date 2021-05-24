# dictionary inside dictionary
user_name = {
    "derrick" : {
        "first-name" : "okinda",
        "last-name" : "kibaso",
        "location" : "Thika town"
    },
    "ojwang": {
        "first-name": "derrick",
        "last-name": "ojwang'",
        "location": "kiang'ombe"
    }
}
for user, user_info in user_name.items():
    print(user + "'s details are:")
    full_name = user_info["first-name"] + "  " + user_info["last-name"]
    location = user_info["location"]
    print(f" full name is:{full_name}")
    print(f"loaction is : {location}")