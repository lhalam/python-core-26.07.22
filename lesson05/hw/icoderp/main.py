# 1. У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен його відгадати
# не більше ніж за 10 спроб. Після кожної невдалої спроби повинно повідомлятися чи більше чи менше
# введене користувачем число, ніж те, що загадане. Якщо за 10 спроб число не відгадане, то вивести загадане число.

import random

attempt = 10
random_number = random.randint(1, 100)
print(random_number)
while attempt != 0:
    user_number = int(input("Enter a number from 1 to 100: "))
    if user_number == 0:
        print("Good bye, you lose!")
        break
    elif user_number == random_number:
        print(f"You win!")
        break
    elif 0 < user_number < 101:
        if user_number > random_number:
            attempt -= 1
            print(f"More, attempt: {attempt}")
        elif user_number < random_number:
            attempt -= 1
            print(f"Less, attempt: {attempt}")
    else:
        attempt -= 1
        print(f"The number must be in the range 1 - 100, attempt: {attempt}")
else:
    print("You lose!")

# 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед
# них чисел, що кратні 5-ти. (не використовувати лісти)

# count = 0
# attempt = 10
# while attempt > 0:
#     user_numbers = int(input(f'Attempt:{attempt}. Enter a numbers n > 2: '))
#     if user_numbers > 2:
#         if user_numbers % 5 == 0:
#             count += 1
#             attempt -= 1
#         else:
#             attempt -= 1
# print(f"Кратні 5-ти: {count}")

# 3. Вивести на екран таблицю множення (від 1 до 9).

# for n in range(2, 10):
#     p = '|'
#     for i in range(1, 10):
#         p += "{:<2}* {:^2}= {:<3}  |  ".format(i, n, i*n)  # f"{i} * {n} = {n*i}\t
#     print(p)

# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
# Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

# n = int(input('Enter a number N: '))
# m = int(input('Enter a number M: '))
# rectangle = []
# for i in range(m):
#     if i == 0:
#         rectangle.append('=' * n)
#     elif i == m - 1:
#         rectangle.append('=' * n)
#     else:
#         rectangle.append(f"={'-'*(n-2)}=")
# for i in rectangle:
#     print(i)

# 5. Дано число P і число H. Користувач вводить послідовність чисел. Визначити: суму тих
# чисел, які менше P; добуток чисел, які більші за H; кількість чисел, що знаходяться в
# діапазоні значень від P до H. При введенні числа рівного P або H, припинити обчислення
# та вивести результат. (не використовувати білдін функції)

# import random
#
# p = random.randint(1, 10)
# h = random.randint(11, 20)
# print(f"P = {p}, H = {h}")
# number_list = []
# sum_p = 0
# diapazon = 0
# dobutock = 1
# :
#     user_number = int(input('Enter a number: '))
#     if user_number == p or user_number == h:
#         for n in number_list:
#             if n < p:
#                 sum_p += n
#             if p < n < h:
#                 diapazon += 1
#             if n > p:
#                 while Truedobutock *= n
#         break
#     else:
#         number_list.append(user_number)
# print(f"Сума чисел, які менші P: {sum_p}\nДобуток чисел, які більші за H: {dobutock}\n"
#       f"Кількість чисел, що знаходяться в діапазоні значень від P до H: {diapazon}")

# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел.
# При введенні числа 0 закінчити роботу.

# number_list = []
# positive = 0
# negative = 0
# while True:
#     user_number = int(input('Enter a number: '))
#     if user_number == 0:
#         print(*number_list)
#         for n in number_list:
#             if n < 0:
#                 negative += 1
#             if n > 0:
#                 positive += 1
#         print(f"Відсоток додатних чисел: {positive * 100 / len(number_list)}%\n"
#               f"Відсоток від’ємних чисел: {negative * 100 / len(number_list)}%")
#         break
#     number_list.append(user_number)
