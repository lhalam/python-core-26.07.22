# Ввести значення(рік), вивести повідомлення "It'saleapyear!"  якщо рік високосний і "Thisisnotaleapyear!" якщо ні.
year = int(input("year >>> "))
if year == 365:
    print("It's a leap year!")
elif year == 366:
    print("This is not a leap year!")

# Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати.
year = int(input("year >>> "))
month = int(input("month >>> "))
day = int(input("day >>> "))
if 0 < year <= 2022:
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 < day <= 31:
        print('Correct')
    elif month in [4, 6, 9, 11] and 1 < day <= 30:
        print('Correct')
    elif month == 2 and (1 < day <= 28 or day == 29):
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')

# Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь
# і якщо так, то видрукувати його
import math
a = int(input("a >>> "))
b = int(input("b >>> "))
c = int(input("c >>> "))
# ax2+bx+c=0
d = b ** 2 - 4 * a * c
print(d)
x1 = None
x2 = None
if d == 0:
    x1, x2 = (-b + math.sqrt(d)) / (2 * a)
    print(x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
else:
    print('No square root')
if x1 != None and x2 != None:
    print(x1, x2)

# Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін;
# Якщо так, то видрукувати його периметр та площу

import math
a = int(input("a >>> "))
b = int(input("b >>> "))
c = int(input("c >>> "))
if (a + b) > c and (b + c) > a and (a + c) > b:
    perimeter = a + b + c
    step_1 = perimeter / 2
    area = math.sqrt(step_1 * (step_1 - a) * (step_1 - b) * (step_1 - c))
    print(perimeter)
    print(area)
else:
    print("wrong triangle")

# Нехай k-ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, ..., суботу чи неділю)
# залежно від того, на який день тижня припадає k-й день не високосного року, в якому 1 січня - понеділок.

k = int(input("k >>> "))
day_in_week = k % 7
if day_in_week == 1:
    n = 'monday'
elif day_in_week == 2:
    n = 'tuesday'
elif day_in_week == 3:
    n = 'wednesday'
elif day_in_week == 4:
    n = 'thursday'
elif day_in_week == 5:
    n = 'friday'
elif day_in_week == 6:
    n = 'saturday'
else:
    n = 'sunday'
print(n)
