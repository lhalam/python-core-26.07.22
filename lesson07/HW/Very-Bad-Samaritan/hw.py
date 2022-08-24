def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a-b
    elif c == "/":
        if b == 0:
            return "Dividing by zero"
        else:
            return a/b
    elif c == "*":
        return a*b
    else:
        return "Unknown operation"


def is_year_leap(year):
    return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False


def square(a):
    return f"Perimeter of a square with length of its side {a}, its area and  diagonal  are  {(4*a, a**2, 2 ** 0.5 *a)}"


def season(number_of_month):
    if number_of_month in [3, 4, 5]:
        return "This is the spring"
    elif number_of_month in [6, 7, 8]:
        return "This is the summer"
    elif number_of_month in [9, 10, 11]:
        return "This is the autumn"
    else:
        return "This is the winter"


def bank(n, years):
    sum = n
    for i in range(0, years):
        sum += 0.1*sum
    return f"In {years} years on your account will be {sum}"


def is_prime(number):
    if number in range(1001):
        for i in range(2, number):
            if number%i == 0:
                return False
        return True
    else:
        return "The number must be between 0 and 1000"


def date(day, month, year):
    if month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        return True
    elif month in {4, 6, 9, 11} and day <= 30:
        return True
    elif (is_year_leap(year) and month == 2 and day <= 29) or (not is_year_leap(year) and month == 2 and day <= 28):
        return True
    else:
        return False


print("Task 1")

# a = float(input("a="))
# b = float(input("b="))
# c = str(input("Action: "))
# print(arithmetic(a, b, c))


print("Task 2")

# print(is_year_leap(int(input("Enter a year:"))))


print("Task 3")

# print(square(int(input("Enter a side of a square:"))))


print("Task 4")

# print(season(int(input("Enter a number of month:"))))


print("Task 5")

# print(bank(int(input("Sum of money =")), int(input("Years ="))))


print("Task 6")

# print(is_prime(int(input("Enter a number ="))))


print("Task 7")

# print(date(int(input("day =")), int(input("month =")), int(input("year ="))))
