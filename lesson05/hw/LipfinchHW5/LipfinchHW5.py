# # 1. У програмі генерується випадкове ціле число від 0 до 100.
# # Користувач повинен його відгадати не більше ніж за 10 спроб.
# # Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# # Якщо за 10 спроб число не відгадане, то вивести загадане число.число
#
# from random import randint
#
# random_number = randint(1, 100)
# number_of_attemps = 10
# while number_of_attemps != 0:
#     guess_number = int(input("Enter number from 1 to 100: "))
#     if random_number == guess_number:
#         print(f"You win, number was{guess_number}")
#         break
#     else:
#         number_of_attemps -= 1
#         print("Your number is bigger" if guess_number > random_number else "Your number is smaller")
# print(f"Random number was {random_number}")
#
# # 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)

# j = 0
# for i in range(10):
#     num = int(input())
#     if num < 2:
#         print("Num must be > 2")
#         continue
#     else:
#         if num % 5 == 0:
#             j += 1
# print(f'There was {j} natural numbers divisible by 5')

# 3. Вивести на екран таблицю множення (від 1 до 9).

# num = int(input())
# for i in range(1, 10):
#    print(num, 'x', i, '=', num*i)

# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")

#Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
#Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

side = int(input("Please Enter any Side of a Square  : "))
i = 0
print("Square Star Pattern")

while(i < side):
    j = 0
    while(j < side):
        j = j + 1
        print('a', end = '  ')
    i = i + 1
    print('')



