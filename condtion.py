language = "python"
if language == "java":
    print("The language is java")
elif language == "python":
    print("language is python")
else:
    print("there is no match at all")

# using the booleans

# and

user = "admin page"
logged_in  =  False
if user and logged_in == True:
    print("welcome admin")

# or

if user or logged_in == True:

    print("it is done")
# not

if not logged_in:
    print("please log in ")

# using is value

a = [1, 2, 3]
b= [1, 2, 3 ]

print(a is  b)