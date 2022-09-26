# CheckEmail

def valid_email(email):
    error = 'Email is not valid'
    email = str(email)
    try:
        if len(email.split('@')) == 2 and email.split('@')[-1] == 'ukr.tel.com':
            print("Email is valid")
        else:
            print(error)
    except RuntimeError:
        print(error)


# valid_email("trafik@ukr.tel.com")
# valid_email("trafik@ukr_tel.com")
# valid_email("tra@fik@ukr.com")
# valid_email(2)


# DayOfWeek


def day_of_week(day):

    day_of_the_week = {1: 'Monday',
                       2: 'Tuesday',
                       3: 'Wednesday',
                       4: 'Thursday',
                       5: 'Friday',
                       6: 'Saturday',
                       7: 'Sunday'}
    try:
        day = int(day)
        print(day_of_the_week[day])
    except ValueError:
        print("You did not enter a number! Please try again.")
    except KeyError or NameError:
        print("There is no such day of the week! Please try again.")


# day_of_week(7)
# day_of_week('Friday')
# day_of_week(17)
# day_of_week("jajshgsj")


# EvenOddNumber

def check_odd_even(number):
    try:
        if number % 2:
            print("Entered number is odd")
        else:
            print("Entered number is even")
    except TypeError:
        print("You entered not a number.")


# check_odd_even(17)
# check_odd_even(228)
# check_odd_even(0)
# check_odd_even("One")


# DivideNumber

def divide(numerator, denominator):
    try:
        print(numerator / denominator)
    except ZeroDivisionError:
        print(f"Oops, {numerator} / {denominator} denominator, division by zero is error!!!")
    except TypeError:
        print("Value Error! You did not enter a number!")


# divide(8, 16)
# divide (5, 0)
# divide("25", 5)
# divide("abc", 9)


# NumberOfGroup

class SmallGroupError(Exception):
    def __init__(self, err_info):
        self.output = err_info

    def __str__(self):
        return self.output


def check_number_group(number):
    try:
        if int(number) > 10:
            print(f"Number of your group {number} is valid")
        elif int(number) <= 10:
            raise SmallGroupError("We obtain error: Number of your group can't be less than 10")
    except SmallGroupError as err:
        print(err)
    except ValueError:
        print("You entered incorrect data. Please try again.")


# check_number_group(4)
# check_number_group(59)
# check_number_group("25")
# check_number_group("abc")


# PositiveNumber

class NegativeOrZeroNumberError(Exception):
    def __init__(self, err_info):
        self.output = err_info

    def __str__(self):
        return self.output


def check_positive(number):
    try:
        if int(number) != 0 and int(number) > 0:
            print(f"You input positive number: {number}")
        else:
            raise NegativeOrZeroNumberError(f"You input negative number: {number}. Try again.")
    except NegativeOrZeroNumberError as err:
        print(err)
    except ValueError:
        print("Error type: ValueError!")


# check_positive(24)
# check_positive(-19)
# check_positive("38")
# check_positive("abc")


# Equation

def solve_quadric_equation(a, b, c):

    try:
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            print(f"The solution are x1 = {x1} and x2 = {x2}")
        elif d == 0:
            print(f"The solution are x = {int(-b / (2*a))}")
        else:
            print('No roots')

    except ZeroDivisionError:
        print("Zero Division Error")
    except TypeError:
        print("Could not convert string to float")


# solve_quadric_equation(1, 5, 6)
# solve_quadric_equation(0, 8, 1)
# solve_quadric_equation(1, "abc", 5)
