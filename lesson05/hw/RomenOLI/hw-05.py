# 1. У програмі генерується випадкове ціле число від 0 до 100.
# Користувач повинен його відгадати не більше ніж за 10 спроб.
# Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# Якщо за 10 спроб число не відгадане, то вивести загадане число.

import random

# n = random.randint(0, 100)
# t = 1
# while t <= 10:
#     print(f"You have {11-t} shots" if (11-t)>1 else "You have last chanse")
#     user_numb = int(input("please, input your number from 0 to 100 - "))
#     if user_numb == n:
#         print(f"Yes, you WIN!!!")
#         break
#     else:
#         print("Nice try, but you didnt guess. Your number is bigger" if user_numb > n else "Nice try, but you didnt guess. Your number is smaller")
#     t += 1
#
# print(f"Random number was - {n}" if t > 10 else "It was great")

# 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)
# count = 0
# for i in range(10):
#     if int(input("input number >2 - ")) % 5 == 0:
#         count +=1
# print(f"there are - {count} number(s) divided 5")

# 3. Вивести на екран таблицю множення (від 1 до 9).


# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
# Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.
# n, m = int(input("input N side - ")), int(input("input M side - "))
# border, zalivka = input("input sign for border - "), input("input sign for filling - ")
# for i in range(n):
#     if i == 0 or i == n-1:
#         print(border * m, end="\n")
#     else:
#         print(border + zalivka * (m-2) + border, end="\n")

# 5. Дано число P  і число H. Користувач вводить послідовність чисел.
# Визначити: суму тих чисел, які менше P;
# добуток чисел, які більші за H;
# кількість чисел, що знаходяться  в діапазоні значень від P до H.
# При введенні числа рівного P або H, припинити обчислення та вивести результат. (не використовувати білдін функції)
p, h = int(input("input number P - ")), int(input("input number H - "))
n = int(input("ВВеди число - "))
sum, count, dob = 0, 0, 1
while n != 0:
    if n == p or n == h:
        print(f"сума чисел, що менші Р = {sum}")
        print(f"добуток чисел, що більше Н = {dob}")
        print(f"кількість чисел, що в діапазоні між Р і Н = {count}")
        break
    elif n<p:
        sum += n
    elif n>h:
        dob *= n

    if p<=n<=h:
        count +=1

    n = int(input("ВВеди число - "))

# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. При введенні числа 0 закінчити роботу.
# dod, vid = 0, 0
# n = int(input("ВВеди число - "))
# while n != 0:
#     if n>0:
#         dod += 1
#     else:
#         vid += 1
#     n = int(input("ВВеди число - "))
# print(f"додаткових чисел = {100 * dod/(dod + vid)}% \nвід’ємних чисел = {100 * vid/(dod + vid)}%")