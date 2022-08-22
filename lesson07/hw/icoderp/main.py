# 1. Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію,
# яка повинна бути здійснена над ними. Якщо третій аргумент +, додати їх; якщо -, то відняти;
# * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок "Невідома операція".

def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Невідома операція"


print(arithmetic(2, 2, '*'))

# 2. Написати функцію is_year_leap, приймає 1 аргумент - рік,
# і повертає True, якщо рік високосний, і False в іншому випадку.

# def is_year_leap(year):
#     return True if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0) else False
#
#
# is_year_leap(2022)

# 3. Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
# і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.

# def square(arg):
#     return (4*arg, arg**2, 2**0.5*arg)
#
#
# print(square(4))

# 4. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
# і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).

# def season(number_of_month):
#     if number_of_month in (1, 2, 12):
#         return "Winter"
#     elif number_of_month in [3, 4, 5]:
#         return "Spring"
#     elif number_of_month in [6, 7, 8]:
#         return "Summer"
#     elif number_of_month in [9, 10, 11]:
#         return "Autumn"
#     else:
#         return "Wrong!!!"
#
#
# print(season(1))

# 5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
# (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу,
# і на них в наступному році теж будуть відсотки). Написати функцію bank, яка приймає
# аргументи n і years, і повертає суму, яка буде на рахунку користувача.

# def bank(n, years):
#     summa = n
#     for i in range(0, years):
#         summa += summa * 0.1
#     return f"Year: {years}, Summa: {summa}"
#
#
# print(bank(100, 2022))

# 6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - в іншому випадку.

# def is_prime(a):
#     if a % a == 0 and a != 0:
#         return True
#     else:
#         return False
#
#
# print(is_prime(55))

# 7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
# Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.

# def is_year_leap(year):
#     return True if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0) else False
#
#
# def date(day, month, year):
#     if month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
#         return True
#     elif month in {4, 6, 9, 11} and day <= 30:
#         return True
#     elif is_year_leap(year) and month == 2 and day <= 29:
#         return True
#     elif not is_year_leap(year) and month == 2 and day <= 28:
#         return True
#     else:
#         return False
#
#
# print(date(24, 8, 2022))
