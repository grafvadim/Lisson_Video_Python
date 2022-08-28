my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

my_dict = {
    "имя": "Виктор", "фамилия": "Петров", "возраст": 45, "цвет глаз": "карие"   
}
print(my_dict["фамилия"])

my_dict["вес"] = 86
my_dict["любимое блюдо"] = "лапша"

print(my_dict)

person = {
    "имя": "Виктор", "рост": 178, "возраст": 27
}
print(person)

person["вес"] = 109
person["любимое блюдо"] = "лапша"
print(person)

del person["любимое блюдо"]
print(person)

for k, v in person.items():
    print(f"{k} >>>> {v}")

for key in person.keys():
    print(key)

if "рост" in person.keys():
    print("Данный ключ уже используется!")
else:
    print("Вы можете использовать данный ключ для создание пары. ")
    
for values in person.values():
    print(values)
print(('-') *10)
    
person = {
    'имя': 'Виктор', 
    'рост': 178, 
    'возраст': 27,
    'любимое блюдо': ['лапша', 'борщ', 'окрошка'],
    'машина': 'Porshe'
}

for values in person['любимое блюдо']:
    print(values)
print(('--') * 50)

persons = {
    "Виктор": { 
        'рост': 178, 
        'возраст': 27,
        'любимое блюдо': ['лапша', 'борщ', 'окрошка'],
        'машина': 'Porshe'
    },
    "Светлана": { 
        'рост': 168, 
        'возраст': 22,
        'любимое блюдо': ['Картошка', 'щи', 'сыр'],
        'машина': 'Opel'
    },
}

for username, userinfo in persons.items():
    print(f"Имя пользователя: {username}")
    age = userinfo["возраст"]
    car = userinfo["машина"]
    
    print(f"Возрат пользователя {username} : {age} лет.")
    print(f"Авто пользователя {username} : {car}\n")
    
print(person)
print(person.get("адрес", "Нет ключа"))

print(person)
print(person.setdefault("адрес"))
print(person)

person.update({"адрес": "СССР"})
print(person)

print(person)
print(person.pop("адрес"))
print(person)

print(person)
print(person.popitem())
print(person)

print(person.keys())
print(person.values())
print(person.items())

person.clear()
print(person)
