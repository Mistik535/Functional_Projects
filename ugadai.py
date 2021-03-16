import random

n = random.randint(0, 10)
print("n", n)
count = 0

while True:
    number = int(input())
    if number > n:
        print("Число больше указанного")
    elif number < n:
        print("Число меньше указанного")
    elif number == n:
        print("Вы угадали число! Выхотите сыграть еще? Да/Нет")

        if "Да" == str(input()):
            n = random.randint(0, 10)
            print("n", n)
        else:
            break


    def binary_search(list, item):
        left = 0
        right = len(list) - 1
        centre = (left + right) / 2

        while left <= right:
            centre = (left + right) / 2
            number = list[centre]
            if number == item:
                return centre
            if number > item:
                right = centre - 1
            else:
                left = centre + 1
            return None
