# creating nested dictionary with for loop

aliens = []
for alien_number  in range (30):
    new_alien = {
        "color" : "green",
        "point" : 7,
        "speed" : "high"
    }
    aliens.append(new_alien)
print(aliens)

for alien in aliens[:5]:
    if alien["color"] == "green":
        alien["color"] == "red"
        alien["point"] == 8
        alien["speed"] == "very high"

    print(alien)