my_list_num = [99, 45, 67, 34, 23, 56, 4, 2, 4,24,10]
my_list_words = ["Сходить за хлебом", "Выпить кофе", "Поспать", "hello", "world"]

print (len  (my_list_words))
print (len (my_list_num))

print(my_list_words[1:3])
print(my_list_num[2:6])

print(my_list_words)
my_list_words.append("Goodbye")
print(my_list_words)

print(my_list_num)
my_list_num.append(95)
print(my_list_num)

print(my_list_words)
my_list_words.insert(2, "Спать")
print(my_list_words)

print(my_list_num)
my_list_num.insert(6, 3)
print(my_list_num)

print(my_list_words)
my_list_words.pop()
print(my_list_words)

my_list_words2 = ["Пожарить шашлык", "Сходить в магазин"]
my_list_words.extend(my_list_words2)
print(my_list_words)

my_list_words3 = my_list_words + my_list_words2
print(my_list_words3)

my_list_words3.remove("Сходить в магазин")
print(my_list_words3)

my_list_num.sort()
print(my_list_num)

my_list_num.reverse()
print(my_list_num)

print(max(my_list_num))
print(min(my_list_num))

my_list_words4 = ' '.join(my_list_words3)
print(my_list_words4)

my_list_words3.clear()
print(my_list_words3)