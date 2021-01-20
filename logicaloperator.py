has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("eligible for loan")
elif has_good_credit or not has_criminal_record:
    print("eligible for loan")
elif has_good_credit and has_high_income and not has_criminal_record:
    print("eligible for loan")
