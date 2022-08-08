# # 1) Вести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний та "It's not a leap year!", якщо рік ні
# import cmath
#
# year = int(input("Enter a year: "))
#
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} It's a leap year".format(year))
# else:
#     print("{0} It's not a leap year".format(year))
#
#
# # 2) Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити
# #   чи введені дані відповідають коректному запису дати.
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# day = int(input("Enter a day:" ))
#
# if year <= 2022:
#     print('')
#     if 1 <= month <= 12:
#         print('')
#         if 1 <=  day <= 31:
#             print('')
#             if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
#                 print('')
#             elif month in [4, 6, 9, 11] and day in range(1, 31):
#                 print('')
#             elif (year % 400 == 0 and month == 2 and day in range(1, 30)) or month == 2 and day in range(1, 29):
#                 print("")
#             else:
#                 print('Enter another day: ')
#
#     else:
#         print('Enter another month:' )
#
# else:
#     print("Enter another year:" )
#
# #3)   Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.
#
# import math

# a, b, c = int(input("Enter number a: ")), int(input("Enter number b: ")), int(input("enter number c: "))
#
# D = b**2 - 4*a*c
# print(D)
#
# if D >= 0:
#     sol = (-b+D**(0.5))/2/a
#     print('Root {0}'.format(sol))
# else:
#     print("No roots")















