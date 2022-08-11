import datetime
import math


def is_leapyear(year):
    print("It's a leap year!" if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0) else "This is not a leap year!")


def check_date(year, month, day):
    try:
        print(datetime.datetime(year, month, day))
    except ValueError:
        print("Дату введено некоректно")


def equation(a, b, c):
    d = b ** b - 4 * a * c
    if d < 0:
        print("Рівняння без коренів")
    elif d == 0:
        print("Рівняння має 1 корень X = ", -b / 2 * a)
    else:
        print("Рівняння має 2 корені X1 = ", (-b - math.sqrt(d)) / 2 * a, "\nX2 = ", (-b + math.sqrt(d)) / 2 * a)


def triangle(a, b, c):
    check = [a, b, c]
    check.sort()
    p = sum(check) / 2
    if check[2] < check[0] + check[1]:
        print("Периметр = ", 2 * p, "\nПлоща = ", math.sqrt(p * (p - check[0]) * (p - check[1]) * (p - check[2])))
    else:
        print("З такими параметрами неможливо побудувати трикутник")


def dayofweek(day):
    match day % 7:
        case 1:
            print("Понеділок")
        case 2:
            print("Вівторок")
        case 3:
            print("Середа")
        case 4:
            print("Четверг")
        case 5:
            print("Пятниця")
        case 6:
            print("Субота")
        case 0:
            print("Неділя")


# Task1
print(is_leapyear(int(input("Введіть рік для перевірки: "))))

# Task2
print(check_date(int(input("Введіть дату для перевірки:\nРік ")),
                 int(input("Місяць")), int(input("День"))))
# Task3
print(equation(int(input("Введіть змінні рівняння:\nA =  ")),
               int(input("B= ")), int(input("C= "))))
# Task4
print(equation(int(input("Введіть сторони трикутника:\na =  ")),
               int(input("b= ")), int(input("c= "))))
# Task5
print(dayofweek(int(input("Введіть число для отримання дня тижня: "))))