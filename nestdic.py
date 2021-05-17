aliens_0 = {
    "color": "green",
    "point": 6

}
alien_1 = {
    "color": "yellow",
    "point": 3
}
alien_2 = {
    "color": "blue",
    "point": 4
}
aliens = [alien_2, alien_1, aliens_0]

for alien in aliens:
    print(alien)

print()
# using range function

alien1 = []
for alien_number in range(30):
    new_alien = {
        "color" : "green",
        "speed" : "medium",
        "point" : 8
    }
    alien1.append(new_alien)

print(alien1, end=" ")

# printing only the first five aliens

for alien_number in alien1[:5]:
    print(alien_number)
