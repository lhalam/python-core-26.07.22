"""1. У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен його відгадати не більше ніж за 10 спроб.
Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
 Якщо за 10 спроб число не відгадане, то вивести загадане число."""

import random

num = random.randint(0, 100)
for i in range(10):
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You win!")
        break
    elif guess < num:
        print("Number is more than one you have entered")
    else:
        print("Number is less than one you have entered")
else:
    print(f"You didn't guess the number. It was {num}.")

"""2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)"""
k = 0
for i in range(10):
    num = int(input("Enter the number n > 2: "))
    if num <= 2:
        print("The number must be more than 2")
        continue
    else:
        if num % 5 == 0:
            k += 1
print(f"Amount of numbers divisible by 5: {k}")

"""3 Вивести на екран таблицю множення (від 1 до 9)."""
for i in range(1, 10):
    for j in range(1, 10):
        print(str(j) + "*" + str(i) + " = " + str(i*j), end = '           ')
    print()

"""4 Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів. 
Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого."""

n = int(input("Enter length of rectangle:  "))
m = int(input("Enter width of rectangle: "))
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1:
            print("*", end="")
        else:
            print("*"+"-"*(m-2)+"*")
            break
    else:
        print()

""" 5 Дано число P і число H. Користувач вводить послідовність чисел. 
Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H;
кількість чисел, що знаходяться в діапазоні значень від P до H.
При введенні числа рівного P або H, припинити обчислення та вивести результат. (не використовувати білдін функції)"""

P = int(input("Enter P: "))
H = int(input("Enter H: "))
s = 0
d = 1
k = 0
x = int(input("Enter number: "))
while x != P and x != H:
    if x < P:
        s += x
    if x > H:
        d *= x
    if x > P and x < H:
        k += 1
    x = int(input("Enter number: "))
print(f"Sum of numbers less then {P} is {s}.")
print(f"Product of numbers more then {H} is {d}.")
print(f"Amount of numbers between {P} and {H} is {k}.")

""" 6 Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. При введенні числа 0 закінчити роботу."""
x = int(input("Enter the number: "))
k_of_positive = 0
all = 0
while x != 0:
   if x > 0:
       k_of_positive += 1
   all += 1
   x = int(input("Enter the number: "))
part_of_positive = k_of_positive/all*100
print(f"Part of positive numbers is {round(part_of_positive, 2)}, part of negative is {round(100 - part_of_positive, 2)}.")



