# using while loops in list
# verifying users
prev_user = ["derrick", "okinda", "kibaso"]
new_users = []
current_user = []
while prev_user:
    new_users = prev_user.pop()
    print(f"verifying: {new_users}")
    current_user.append(new_users)
print("the following users  have been confirmed:")
for user in current_user:
    print(user)
print()
# Removing All Instances of Specific Values from a List
pets = ["cats", "pigs", "dogs", "horse", "cats", "cats", "cats"]
while "cats" in pets:
    pets.remove("cats")
print(pets)