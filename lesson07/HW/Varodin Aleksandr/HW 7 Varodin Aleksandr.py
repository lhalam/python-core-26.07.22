# Task 1

def arithmetic(number_1, operation, number_2):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '*':
        return number_1 * number_2
    elif operation == '/':
        return number_1 / number_2
    else:
        return "Невідома операція"
print(arithmetic(12, '=', 2))

# Task 2

def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
print(is_year_leap(1997))

# Task 3

import math
def square(quad):
    perimetr = quad * 4
    ploshad = quad ** 2
    diagonal = quad * math.sqrt(2)
    return (perimetr, ploshad,diagonal)
print(square(6))

# Task 4

def season(month):
    if month == 12 or month == 1 or month == 2:
        return 'Winter'
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return 'Summer'
    elif month == 9 or month == 10 or month == 11:
        return 'Autumn'
    else:
        return 'Error'
print(season(9))

# Task 5

def bank(n, years):
    count = 1
    while count != years:
        n = n / 100 * 10 + n
        count += 1
    return n
print(bank(500, 3))

# Task 6

def is_prime(number):
    delitel = [2, 3, 5, 7]
    if number == 1:
        return False
    if number not in delitel:
        for i in delitel:
            if number % i != 0:
                return False
    return True
print(is_prime(1))

# Task 7

def date(day, month, year):
    if year == 2022:
        if 1 <= month <= 12:
            if 1 <= day <= 28 or 1 <= day <= 30 or 1 <= day <= 31:
                return True
            else:
                return False
print(date(12,11,2022))

