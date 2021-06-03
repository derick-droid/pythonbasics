# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches . Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ["tuna", "Classic club", "Ham and Cheese"]
finished_sandwiches = []
while sandwich_orders:
    making_sandwiches = sandwich_orders.pop()
    print(f"I made your {making_sandwiches}")
    finished_sandwiches.append(making_sandwiches)

print()
for sandwich in finished_sandwiches:
    print(f"I made {sandwich} very delicious")