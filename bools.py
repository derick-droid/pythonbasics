
# showing how to use data type in python
def are_you_sad(is_raining, has_umbrella):
    if is_raining and not has_umbrella:
        print(True)
    else:
        print(False)


are_you_sad(True, False)
are_you_sad(True, True)

# more exercise


def c_greater_than_d_plus_e(c, d, e):
    # c= 48
    # d = 3
    # e = 8
    d_plus_e = d + e

    if c > d_plus_e:
        print(True)
    else:
        print(False)


c_greater_than_d_plus_e(48, 3, 8)
c_greater_than_d_plus_e(1, 5, 8)
