# # # 1) Вести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний та "It's not a leap year!", якщо рік ні
#

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} It's a leap year".format(year))
else:
    print("{0} It's not a leap year".format(year))
#
# #
# # # 2) Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити
# # #   чи введені дані відповідають коректному запису дати.
# #
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day:" ))

if year <= 2022:
    print('')
    if 1 <= month <= 12:
        print('')
        if 1 <= day <= 31:
            print('')
            if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                print('')
            elif month in [4, 6, 9, 11] and day in range(1, 31):
                print('')
            elif (year % 400 == 0 and month == 2 and day in range(1, 30)) or month == 2 and day in range(1, 29):
                print("")
            else:
                print('Enter another day: ')

    else:
        print('Enter another month:' )

else:
    print("Enter another year:" )
# #
# # #3)   Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.
# #
import cmath

a, b, c = int(input("Enter number a: ")), int(input("Enter number b: ")), int(input("enter number c: "))

D = b**2 - 4*a*c
print(D)

if D >= 0:
    sol = (-b-cmath.sqrt(D))/(2*a)
    sol2 = (-b+cmath.sqrt(D))/(2*a)
    print('Root {0}'.format(sol,sol2))
else:
    print("No roots")
#
# #4) Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін; Якщо так, то видрукувати його периметр та площу.

a, b, c = int(input("Enter first side a: ")), int(input("Enter second side b: ")), int(input("enter third side c: "))
if a ** 2 + b ** 2 == c ** 2:
    print("yes")
    P = a + b + c
    p = P / 2
    S = (p*(p-a)*(p-b)*(p-c) ** 0.5)
    print("Perimeter = {0}".format(p))
    print("Area of triangle = {0}".format(S))

else:
    print("no, you can't")
#
# # Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який
# # # день тижня припадає k-й день не високосного року, в якому 1 січня - понеділок
#
k = int(input())
weekday = k % 7

match weekday:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')







