#Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні
import math

def is_lipyear(year):
    text = ""
    if year % 4 == 0:
        if year % 100 != 0:
            text = "It's a leap year!"
        else:
            if year % 400 == 0:
                text = "It's a leap year!"
            else:
                text = "This is not a leap year!"
    else:
        text = "This is not a leap year!"
    return text

print(is_lipyear(int(input("please, input year - "))))

#Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати
year, month, day = int(input("input year  - ")), int(input("input month  - ")), int(input("input day  - "))

if month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
    print("It is correct date")
elif month in (4, 6, 8, 11) and day <= 30:
    print("It is correct date")
elif month == 2:
    if (is_lipyear(year) == "It's a leap year!" and day <= 29) or (is_lipyear(year) != "It's a leap year!" and day <= 28):
        print("It is correct date")
    else:
        print("It is not correct date")
else:
    print("It is not correct date")

# Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.
a, b, c = int(input("введи число a - ")), int(input("введи число b - ")), int(input("введи число c - ")),
d = b**2 - 4*a*c

if d > 0:
    print(f"корінь: {(-b + math.sqrt(d))/(2*a)}")
elif d == 0:
    print(f"корінь: {-b / (2 * a)}")
else:
    print("немає дійсних коренів")

# Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін; Якщо так, то видрукувати його периметр та площу.

a, b, c = float(input("введи сторону трикутника a - ")), float(input("введи сторону трикутника b - ")), float(input("введи сторону трикутника c - ")),
if a > 0 and b > 0 and c > 0:
    if a+b >c and a+c > b and b+c > a:
        print(f"периметр - {a+b+c}")
        p = (a+b+c)/2
        pl = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(f"площа - {pl}")
    else:
        print("it is not a triangle")
else:
    print("it is not a triangle")

# Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який
# день тижня припадає k-й день не високосного року, в якому 1 січня - понеділок
k = int(input("введи число від 1 до 365 - "))
match k%7:
    case 1:
        n = "понеділок"
    case 2:
        n = "вівторок"
    case 3:
        n = "середа"
    case 4:
        n = "четвер"
    case 5:
        n = "пятниця"
    case 6:
        n = "субота"
    case 0:
        n = "неділя"

print(f"{k} - припадає на {n}")