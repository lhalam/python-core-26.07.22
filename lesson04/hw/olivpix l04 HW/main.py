# 1.Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні.
yearcheck = int(input("Check "))
if yearcheck % 4 == 0:
    print("It's a leap year!")
else:
    print("This is not a leap year!")

# 2.Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати.
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
if month in [1, 3, 5, 7, 8, 10, 12] and 0<day<=31:
    print("OK")
elif month in [4, 6, 9, 11] and 0<day<=30:
    print("OK")
elif year%4!=0 and month in [2] and 0<day<=28:
    print("OK")
elif year%4==0 and month in [2] and 0<day<=29:
    print("OK")
else:
    print("Error")

# Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.
import math

a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
D=b**2-4*a*c
if D>0:
    x1 = (-b+math.sqrt(D)) / (2 * a)
    x2 = (-b-math.sqrt(D)) / (2 * a)
    print(f"There is two square roots. \n x1 = {x1} \n x2 = {x2}")
elif D==0:
    x1 = (-b) / (2*a)
    print(f"There is one square root. \n x1 = {x1}")
else:
    print("numbers has no square root")

# Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін;
# Якщо так, то видрукувати його периметр та площу.
print("Enter the length of triangle sides")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a+b>c and b+c>a and a+c>b:
    P = a+b+c
    p = P/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Triangle has a correct length of sides.\n P = {P} \n S = {S}")
else:
    print("Wrong length of triangle sides.")

# Нехай k- ціле від 1 до 365.
# Присвоїти цілій змінній n значення (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який день тижня
# припадає k-й день не високосного року, в якому 1 січня - понеділок.

day = int(input("Enter the day from 1 to 365 to check the day of the week:"))
if day>0 and day<=365:
    day= day%7
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Tuesday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
else:
    print("wrong number")