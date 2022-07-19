# Пробуем строки

string_x = 'Привет всем от "Чайки"'
string_x2 = "Hello all, \"Chayka\""
print(string_x)
print(string_x2)

string_x3 = string_x + string_x2
print(string_x3)

name = 'Go '
print(name * 20)

my_string = 'Python'
for mtg in dir(my_string):
    print(mtg)
    
print('#' * 28)

my_string = my_string.upper()
print(my_string)
print('-' * 30)
my_string = my_string.lower()
print(my_string)
print('-' * 30)
my_string = my_string.title()
print(my_string)
print('-' * 30)

my_string = 'My city Doneck'
print(my_string)
my_string = my_string.replace('Doneck', 'Krefild')
print(my_string)

print('-' * 30)

my_string = 'My city Doneck'
print(my_string)
my_string = my_string.split(' ')
print(my_string)
print(f'Тип my_string: {type(my_string)}')

my_string = ' '.join(my_string)
print(my_string)

my_string = ' I like Python'
my_string = my_string.strip()
print(my_string)

name = 'Федор'
name_1 = 'Анна'
my_string = f'Привет {name}, {name_1}'
print(my_string)