#1. Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
# Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге).
# В інших випадках повернути рядок "Невідома операція".

# def arithmetic(a, b, o):
#     """
#     Arithnetic operations with numbers
#     :param a: number
#     :param b: number
#     :param o: string - arithmetic operation
#     :return:
#     """
#     res = 0
#     match o:
#         case "-":
#             res = a - b
#         case "+":
#             res = a + b
#         case "*":
#             res = a * b
#         case "/":
#             res = a / b
#         case _:
#             res = "Невідома операція"
#     return res
#
# print(arithmetic(int(input("input first number - ")), int(input("input first number - ")), input("input operation sign: ")))

# Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і False в іншому випадку.

# def is_year_leap(year: int) -> bool:
#     text = ""
#     if year % 4 == 0:
#         if year % 100 != 0:
#             text = True
#         else:
#             if year % 400 == 0:
#                 text = True
#             else:
#                 text = False
#     else:
#         text = False
#     return text
#
# print(is_year_leap(int(input("input year - "))))

# Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
# і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.

def square(side: int) -> tuple:
    from math import sqrt
    return side*4, side**2, side * sqrt(2)

print(*square(int(input("input side of square - "))), sep="\n")

# Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).
#
# Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки). Написати функцію bank, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.
#
# Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і False - в іншому випадку.
#
# Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.