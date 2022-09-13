"CheckEmail" #1
def valid_email(email):
    error = 'Email is not valid'
    try:
        if len(email.split('@')) == 2 and email.split('@')[-1] == 'ukr.tel.com':
            print("Email is valid")
        else:
            print(error)
    except:
        print(error)

# valid_email("trafik@ukr.tel.com")
# valid_email("trafik@ukr_tel.com")
# valid_email("tra@fik@ukr.com")
# valid_email("ownsite@our.c0m")

"DayOfWeek" #2
def day_of_week(day):

    day_of_the_week = {1: 'monday',
                       2: 'tuesday',
                       3: 'wednesday',
                       4: 'thursday',
                       5: 'friday',
                       6: 'saturday',
                       7: 'sunday'}
    try:
        day = int(day)
        print(day_of_the_week[day])
    except ValueError:
        print("'You did not enter a number! Please try again.'")
    except KeyError or NameError:
        print("'There is no such day of the week! Please try again.'")

# day_of_week(9)
# day_of_week('monday')
# day_of_week(4)

'EvenOddNumber' #3
def check_odd_even(number):
    try:
        if number % 2:
            print("Entered number is odd")
        else:
            print("Entered number is even")
    except TypeError:
        print("You entered not a number.")

# check_odd_even(17)
# check_odd_even(18)
# check_odd_even('fus')

"DivideNumber" #4
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

'NumberOfGroup' #5
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

'PositiveNumber' #6
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

'Equation' #7
def solve_quadric_equation(a, b, c):

    try:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + D*0.5) / (2*a)
            x2 = (-b - D*0.5) / (2*a)
            print(f"The solution are x1 = {x1} and x2 = {x2}")
        elif D == 0:
            print(f"The solution are x = {int(-b / (2*a))}")
        else:
            print('No roots')

    except ZeroDivisionError:
        print("Zero Division Error")
    except TypeError:
        print("Could not convert string to float")

# solve_quadric_equation(1, 5, 6)
# solve_quadric_equation(0, 8, 1)
# solve_quadric_equation(1,"abc", 5)