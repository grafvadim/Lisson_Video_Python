# Певое задание
print('Добро пожаловать на борт "Чайки", \Капитан\ ')

# Второе задание
name = input("Input Name: ")
healt = int(input("Healt: "))
ammo = input("Ammo - Yes or No? ")

# print("Name", ": ", name)
# print("Healt", ": ", healt)
if ammo == "yes":
    # print("Ammo", ": ", "Yes")
    ammo_gun = int(input("Ammo gun: "))
    print("Name", ": ", name)
    print("Healt", ": ", healt)
    print("Ammo", ": ", "Yes")
    print("Ammo gun ", ammo_gun)
else:
    print("Ammo", ": ", "No")