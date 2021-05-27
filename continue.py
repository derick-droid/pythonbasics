# using continue in while loops .continue is used to tell python to ignore the code and move the beginning of the loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)