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

#2. Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і False в іншому випадку.

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

#3. Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
# і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.

# def square(side: int) -> tuple:
#     from math import sqrt
#     return side*4, side**2, side * sqrt(2)
#
# print(*square(int(input("input side of square - "))), sep="\n")

#4. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року,
# якій цей місяць належить (зима, весна, літо або осінь).

# def season(month: int) ->str:
#     res = ""
#     match month:
#         case 12 | 1 | 2:
#             res = "зима"
#         case 3 | 4 | 5:
#             res = "весна"
#         case 6 | 7 | 8:
#             res = "літо"
#         case 9 | 10 | 11:
#             res = "осінь"
#         case _:
#             res = "wrong month number"
#     return res
#
# print(season(int(input("input month number (1-12) - "))))

#5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
# (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).
# Написати функцію bank, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.

# def bank(n, years):
#     for x in range(years):
#         n += (n * 10)/100
#     return n
#
# print("Your final amout is - ",bank(int(input("input amount of deposit- ")),int(input("input term of deposit- "))))

#6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - в іншому випадку.

# def is_prime(n) -> bool:
#     count = 0
#     for i in range(1, n + 1):
#         if n%i == 0:
#             count += 1
#     return True if count == 2 else False
#
#
# print("Yes, its prime" if is_prime(int(input("input number from 0 - 1000: "))) else "No it is not prime")

#7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
# Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.

def date(day, month, year):

    return True

print(date(int(input("input day - ")),int(input("input month - ")),int(input("input year - "))))