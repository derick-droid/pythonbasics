names = ["paul", "derrick", "enock", "dave"]
for name in names:
    print(name)
# USING THE RANGE FUNCTIONS

for items in range (100): # THE FUNCTION IS USED TO WIDE RANGE OF VALUES RATHER THAN CODING
    print(items)
# USING RANGE FUNCTIONS TO OUTPUT SEQUENCE OF NUMBERS

for items in range (2,10,2):
    print(items)
# EXERCISE -- CALCULATING SUM OF PRICE IN A SHOPPING LIST
prices = [20, 30, 29, 647, 974,]
value = 0
for price in prices:
    value += price
print(f"value: {value} ")