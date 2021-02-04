def large_number(base_number, power_number):
    result = 1
    for index in range(power_number):
        result = result * base_number
    return result


print(large_number(3, 2))


