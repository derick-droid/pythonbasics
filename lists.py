# BASIC IN LST
name = ["derrick", "john", "mosh", "sarah"]
print(name)

# USING INDEX TO RETRIEVE VALUE FROM A LIST

name = ["derrick", "john", "mosh", "sarah"]
print(name[0])  # PRINTING VALUE AT INDEX ZERO
print(name[2:])  # PRINTING VALUE FROM INDEX 2 TO THE LAST INDEX IN THE LIST
print(name[:])  # PRINTS THE WHOLE VALUE IN A LISTS
print(name[1:3])  # PRINTING VALUE FROM INDEX 1 TO INDEX 3 BUT IGNORES THE VALUE AT 3RD INDEX
name[0] ="jon"
print(name)  # CORRECTING AN ERROR MADE IN LIST

# LIST EXERCISE
# FINDING THE LARGEST VALUE IN A LIST
numbers = [13332,7353,38373,9837,34353,29277,3535637,]
great_value = 0
for number in numbers:
    if number > great_value:
        great_value = number
print(f"the largets value: {great_value} ")

