#1. Написати функцію arithmetic, яка приймає 3 аргументи:
# перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
# Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге).
# В інших випадках повернути рядок "Невідома операція".


#2. Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний,
# і False в іншому випадку.

# def is_year_leap():
#     is_year_leap = int(input())
#     if is_year_leap % 4 == 0 and is_year_leap % 100 != 0:
#         return True
#     else:
#         return False
# print(is_year_leap())

#3. Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площу квадрата і діагональ квадрата.

# def square():
#     i


#4. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
# і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь)."

# def season():
#     month = int(input("Enter month: "))
#     if month in [12, 1, 2]:
#         return 'winter'
#     elif month in [3, 4, 5]:
#         return 'spring'
#     elif month in [6, 7, 8]:
#         return 'summer'
#     elif month in [9, 10, 11]:
#         return 'autumn'
#     else:
#         return 'Wrong month'
# print(season())

#5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%.
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки). Написати функцію bank, яка приймає аргументи n і years,
#і повертає суму, яка буде на рахунку користувача."

# def invest(money, years):
#     for i in range(years):
#         money += money*0.1
#     return f'your balance will be {money}, for {years} years'
# print(invest(10, 10))

#6.Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - в іншому випадку.

# def if_prime(numb):
#     if numb in range(1001):
#         for i in range(1, numb):
#             if numb % i == 0:
#                 return False
#         else:
#                 return True
# print(if_prime(100))

#7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True,
# якщо така дата є в нашому календарі, і False - в іншому випадку.

def date(day, month, year):
    if year <= 2022:
        if 1 <= month <= 12:
            if 1 <= day <= 31:
                if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                    print('')
                elif month in [4, 6, 9, 11] and day in range(1, 31):
                    print('')
                elif (year % 400 == 0 and month == 2 and day in range(1, 30)) or month == 2 and day in range(1, 29):
                    print('')
                return True
    else:
        return False
print(date(12, 8, 90))











