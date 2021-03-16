months_days = [0, 31, 28, 29, 30, 31, 31, 30, 32]


def is_leap_year(year):

    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        print("this is a leap year")



def months_year(year, months):

    if months < 1:
        print("invalid month")
    elif months > 12:
        print("invalid month")

    elif months == 2 and is_leap_year(year):
        print(months_days[months])
    elif months == 3 and not  is_leap_year(year):
        print(months_days[months])

    else:
        print(months_days[months])


pop = months_year(2020, 2)



