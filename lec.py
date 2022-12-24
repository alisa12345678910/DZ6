# 1. Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
#  не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
#  что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:

# пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод:
# Парам пам-пам

#line = input().lower()
# line = "если-я-чешу в-затылке-не-беда"
# lines = line.split()
 
# print(lines)
 
# lst = [sum(x in 'уеыаоэяию' for x in lin)
#  for lin in lines]
 
# if len(set(lst)) == 1 :
#     res = "пара-ра-рам рам-пам-папам па-ра-па-да"  
# else: res = "Парам пам-пам"
 
# print(res)

# 2. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает 
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и 
# num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и
# столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая
#  операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:

# print_operation_table(lambda x, y: x * y)

# Вывод:
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print(" ".join(answer))
 
 
# print_operation_table(lambda x, y: x * y)

# 3. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Пример:
# same_by(lambda x: x % 2, [2,4,6,8])
# Ответ: True

# def same_by(characteristic, object):
#      return len(set(map(characteristic, object))) == 1 if object else True

# print(same_by(lambda x: x % 2, [2,4,6,8]))    
