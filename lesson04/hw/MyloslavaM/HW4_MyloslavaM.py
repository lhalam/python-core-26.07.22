# task 1 Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні.
#
# year = int(input())
# if year == 365:
#     print("This is not a leap year!")
# elif year == 366:
#     print("It is a leap year!")
# else:
#     print("No data")


# task 2 Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати.

# year = int(input())
# month = int(input())
# day = int(input())
# if year <= 1000:
#     if month in (1, 3, 5, 7, 8, 10, 12) and 0 < day <= 31:
#         print("Correct Data")
#     elif month in (4, 6, 9, 11) and 0 < day <= 30:
#         print("Correct Data")
#     elif month == 2 and (0 < day <= 28 or day == 29):
#         print("Correct Data")
#     else:
#         print("no data")

# task 3 ?

# task 4 Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін; Якщо так,
# то видрукувати його периметр та площу.
# import math
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
# if (a + b) > c and (b + c) > a and (c + a) > b:
#     perimeter = (a + b + c)
#     h_p = (a + b + c) / 2
#     area = math.sqrt(h_p * (h_p - a) * (h_p - b) * (h_p - c))
#     print(perimeter)
#     print(area)
# else:
#     print("triangle does not exist")

# task 5 Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, ..., суботу чи неділю)
# залежно від того , на який день тижня припадає k-й день не високосного року, в якому 1 січня - понеділок.

k = int(input())
day_of_week = k % 7
if day_of_week == 1:
    print("monday")
elif day_of_week == 2:
    print("tuesday")
elif day_of_week == 3:
    print("wensday")
elif day_of_week == 4:
    print("thursday")
elif day_of_week == 5:
    print("friday")
elif day_of_week == 6:
    print("saturday")
else:
    print("sunday")
