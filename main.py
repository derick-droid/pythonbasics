# exceptions helps to limit codes from crushing
try:
    age = int(input("age: "))
    income = 20000
    rate  = income // age
    print(age)
    print(rate)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("invalid age value")
