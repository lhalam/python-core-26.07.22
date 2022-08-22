from math import sqrt
import datetime


# task1
def arithmetic(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "/ 00 disaster"
            return a / b
        case _:
            return "Incorrect input"


arithmetic(2, 3, '*')


# task2
def is_year_leap(year):
    print("It's a leap year!" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "This is not a leap year!")


is_year_leap(2022)


# task3
def square(x):
    return x * 4, x ** 2, x * sqrt(2)


print(*square(5))


# task4
def season(month):
    match month:
        case 1 | 2 | 12:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Літо"
        case 9 | 10 | 11:
            return "Осінь"


print(season(10))


# task5
def bank(n, years):
    for i in range(years):
        n = n + (n * 0.1)
    return n


print(bank(78, 20))


# task6
def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    else:
        return True


print(is_prime(745))


# task7
def date(year, month, day):
    try:
        print(datetime.datetime(year, month, day))
    except ValueError:
        print("Некоректна дата")


print(date(72, 13, 2034))
