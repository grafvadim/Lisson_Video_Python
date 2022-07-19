x = 20
y = 2.5
print(f'Тип x: {type(x)}')
print(f'Тип y: {type(y)}')

print('#' * 28)

x = 22 / 7
print(x)

print('#' * 28)

x = 22 // 7
print(x)

print('#' * 28)

x = 10 % 7
print(x)

def myfunc(num):
    if num % 2 == 0:
        print(f"Число {num} четное!")
    else:
        print(f"Число {num} не четное!")
myfunc(678)

print('#' * 28)

x = int(10.47798789789)
print(x)
print(f'Тип x: {type(x)}')

print('#' * 28)

x = float(30)
print(x)
print(f'Тип x: {type(x)}')

print('#' * 28)

x = 22 / 7
x = round(x, 1)
print(x)

print('#' * 28)

x = abs(-54)
print(x)

print('#' * 28)

x = min(1, 5, 7, 44, 9)
print(x)

print('#' * 28)

x = max(1, 2, 55, 76, 5, 34, 345)
print(x)