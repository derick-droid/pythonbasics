# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car = input("what car do you want: ")
print(f"let me see if I can get {car}")
print()
# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

people = int(input("how many people are in your dinner group: "))
if people > 8:
    print("sorry you will have to wait for a table")
else:
    print("The table is ready")
print()

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = int(input("enter number: "))
if number % 10 == 0:
    print("it is multiple of 10")
else:
    print("not multiple of 10")