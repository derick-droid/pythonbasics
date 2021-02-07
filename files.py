# checking files in python
open("employee.txt",  "r") # to read the existing file
open("employee.txt", "a") # to append information into a file
employee = open("employee.txt",  "r")
# employee.close()  # after opening a file  we close the file

print(employee.readable())  # this is to check if the file is readable
print(employee.readline())  # this helps read the first line

print(employee.readline())  # this helps to read the second line after the first line
print(employee.readline()[0])  # accessing specific data from the array

# looping through a file in  python
for employees in employee.readline():
    print(employee)

# adding information into a file
employee = open("employee.txt", "a")
print(employee.write("\n derrick -- for ICT department"))
employee.close()

# re writing a new file or overwriting a file
employee = open("employee1.txt", "w")
employee.write("kelly -- new manager")


 
