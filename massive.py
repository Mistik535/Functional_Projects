# mas = [2, 3, 7, 8, 10]
# for i in range(2, 7):
#     for k in range(len(mas)):
#         a = mas[k] * i
#         print(a, end=" ")

# def recursion(x):
#     print("begin: ", x)
#     if x == 10:
#         print("end: ", x)
#         return None
#     x += 1
#     print("prev: ", x)
#     recursion(x)

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in list_1:
#     if elem < 5:
#         print(elem, end=" ")

# Задача 2.
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = [elem for elem in a if elem in b]
# print(result)

# Игра будет следующей — компьютер загадывает число в диапазоне, заданном пользователем.
# Пользователь пытается угадать число, при этом компьютер сообщает больше загаданное число или меньше.
# Кроме того, программа выводит минимальное количество шагов, за которое можно было отгадать.
# И конечно же предлагает сыграть еще.

# import random
#
# n = random.randint(0, 100)
# number = int(input())
#
# def binary_search(list, item):
#     left = 0
#     right = len(list) - 1
#     centre = (left + right) / 2
#
#     while left <= right:
#         centre = (left + right) / 2
#         number = list[centre]
#         if number == item:
#             return centre
#         if number > item:
#             right = centre - 1
#         else:
#             left = centre + 1
#         return None

voted = {"1": "tom"}
a = str(input())

def check_voter(voted):
    if voted.get(voted):
        print("kick them out!")
    else:
        voted[a] = True
        print("let them vote!")

check_voter(a)

# cache = {}
# def get_page(url):
#  if cache.get(url):
#  return cache[url] #Возвращаются кэшированные данные
#  else:
#     data = get_data_from_server(url)
#     cache[url] = data #Данные сначала сохраняются в кэше
#     return data

# d_list = {"1": "Moscow", "2": "Prague", "3": "London", "4": "Berlin"}
