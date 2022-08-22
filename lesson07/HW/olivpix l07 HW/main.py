import math
# 1. Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
# Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге).
# В інших випадках повернути рядок "Невідома операція".

def arithmetic(a, b, operation):
    if operation=="+":
        print(f"\t{a} + {b} = {a+b}")
    elif operation=="-":
        print(f"\t{a} - {b} = {a-b}")
    elif operation=="*":
        print(f"\t{a} * {b} = {a*b}")
    elif operation=="/":
        print(f"\t{a} / {b} = {a/b}")
    else:
        print("Невідома операція")

arithmetic(4, 6, "**")

# 2.Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і False в іншому випадку.
def is_year_leap(year):
    if (year % 400 == 0 or year % 100 != 0) and year % 4 == 0:
        return True
    else:
        return False
print(is_year_leap(1764))

# 3.Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площу квадрата і діагональ квадрата.

def sqare(side):
    P = 4 * side
    S = side ** 2
    d = side * math.sqrt(2)
    return (P, S, d)
print(sqare(5))

# 4.Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить
# (зима, весна, літо або осінь).
def season(month_num):
    match month_num:
        case 1|2|12:
            return "Зима"
        case 3|4|5:
            return "Весна"
        case 6|7|8:
            return "Літо"
        case 9|10|11:
            return "Осінь"
print(season(2))

# 5.Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%.
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).
# Написати функцію bank, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.

def bank(n, years):
    for i in range(years):
        n=n+(n*0.1)
    return n
print(bank(100, 2))

# 6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і False - в іншому випадку.
def is_prime(num):
    i=2
    while i<(num):
        if num % i == 0:
            return False
        else:
            i += 1
    else:
        return True
print(is_prime(863))
# 7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
# Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.
def date(day, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:
        return True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        return True
    elif (year % 400 == 0 or year % 100 != 0) and year % 4 == 0 and month in [2] and 0 < day <= 29:
        return True
    elif month in [2] and 0 < day <= 28:
        return True
    else:
        return False
print(date(29, 2, 2024))