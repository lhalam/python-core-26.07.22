# CheckEmail

def valid_email(email):
    message = 'Email is not valid'
    try:
        if len(email.split('@')) == 2 and email.isascii():
            user_info, domain_info = email.split('@')
            if domain_info.count('.') in (1, 2):
                domain_info = domain_info.split('.')
                for i in range(len(domain_info)):
                    if domain_info[i] == 'com':
                        continue
                    elif domain_info[i].isalpha():
                        message = 'Email is valid'
                    else:
                        message = 'Email is not valid'
            else:
                message = 'Email is not valid'
        else:
            message = 'Email is not valid'
    except:
        message = 'Email is not valid'
    return message


# import re
#
# def valid_email(email):
#     result = re.findall(r'\b[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]{2,}', email)
#     if len(result) != 0:
#         return 'Email is valid'
#     else:
#         return 'Email is not valid'


print(valid_email("trafik@ukr.tel.com")) #output: "Email is valid"
print(valid_email("trafik@ukr_tel.com")) #output: "Email is not valid"
print(valid_email("tra@fik@ukr.com")) #output: "Email is not valid"
print(valid_email("ownsite@our.c0m")) #output: "Email is not valid"


# DayOfWeek

# class NoDayInWeekError(ValueError):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return self.data
#
#
# def day_of_week(day):
#     try:
#         if day > 7 or day < 0:
#             raise NoDayInWeekError("There is no such day of the week! Please try again.")
#     except NoDayInWeekError as err:
#         print(err)
#     except TypeError:
#         print('You did not enter a number! Please try again.')
#     else:
#         if day == 1:
#             print('Monday')
#         elif day == 2:
#             print('Tuesday')
#         elif day == 3:
#             print('Wednesday')
#         elif day == 4:
#             print('Thursday')
#         elif day == 5:
#             print('Friday')
#         elif day == 6:
#             print('Saturday')
#         elif day == 7:
#             print('sunday')
#
#
# day_of_week(2) # output: "Tuesday"
# day_of_week(11) # output: "There is no such day of the week! Please try again."
# day_of_week("Monday") # output: "You did not enter a number! Please try again."


# EvenOddNumber

# def check_odd_even(number):
#     try:
#         if number % 2 == 0:
#             print("Entered number is even")
#         else:
#             print("Entered number is odd")
#     except TypeError:
#         print("You entered not a number.")
#
# check_odd_even(24)  #output: "Entered number is even"
# check_odd_even(19)  #output: "Entered number is odd"
# check_odd_even('q')  #output: "You entered not a number."


# DivideNumber

# class ZeroError(ZeroDivisionError):
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
#
#     def __str__(self):
#         if self.n1 == 0:
#             return f"Oops, {self.n1} / {self.n2} numerator, division by zero is error!!!"
#         elif self.n2 == 0:
#             return f"Oops, {self.n1} / {self.n2} denominator, division by zero is error!!!"
#
#
# def divide(numerator, denominator):
#     try:
#         if numerator == 0 or denominator == 0:
#             raise ZeroError(numerator, denominator)
#         print(numerator / denominator)
#     except ZeroError as err:
#         print(err)
#     except TypeError:
#         print("Value Error! You did not enter a number!")
#
#
# divide(8, 16) #output: "Result is 0.5"
# divide (5, 0) #output: "Oops, 5 / 0 denominator, division by zero is error!!!"
# divide("25", 5) #output: "Value Error! You did not enter a number!"
# divide("abc", 9) #output: "Value Error! You did not enter a number!"


# NumberOfGroup

# class ToSmallNumberGroupError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return self.data
#
#
# def check_number_group(number):
#     try:
#         if int(number) > 10:
#             print(f"Number of your group {number} is valid")
#         elif int(number) <= 10:
#             raise ToSmallNumberGroupError("We obtain error: Number of your group can't be less than 10")
#     except ToSmallNumberGroupError as err:
#         print(err)
#     except ValueError:
#         print("You entered incorrect data. Please try again.")
#
#
# check_number_group(4) #output: "We obtain error: Number of your group can't be less than 10 "
# check_number_group(59) #output: "Number of your group 59 is valid"
# check_number_group("25") #output: "Number of your group 25 is valid"
# check_number_group("abc") #output: "You entered incorrect data. Please try again."


# PositiveNumber

# class MyError(Exception):
#     def __init__(self, data):
#             self.data = data
#     def __str__(self):
#         return self.data
#
#
# def check_positive(number):
#     try:
#         if int(number) > 0:
#             print(f"You input positive number: {number}")
#         elif int(number) < 0:
#             raise MyError(f"You input negative number: {number}. Try again.")
#     except MyError as err:
#         print(err)
#     except ValueError:
#         print("Error type: ValueError!")
#
#
# check_positive(24) #output: "You input positive number: 24"
# check_positive(-19) #output: "You input negative number: -19. Try again."
# check_positive("38") #output: "You input positive number: 38"
# check_positive("abc") #output: "Error type: ValueError!"


# Equation

# import math
#
#
# def solve_quadric_equation(a, b, c):
#     try:
#         d = b ** 2 - 4 * a * c
#         x1 = None
#         x2 = None
#         if d == 0:
#             x1, x2 = (-b + math.sqrt(d)) / (2 * a)
#         elif d > 0:
#             x1 = (-b + math.sqrt(d)) / (2 * a)
#             x2 = (-b - math.sqrt(d)) / (2 * a)
#         else:
#             print('No square root')
#         if x1 != None and x2 != None:
#             print(f"The solution are x1=({-2}-0j) and x2=({-3}+0j)")
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except TypeError:
#         print("Could not convert string to float")
#
#
# solve_quadric_equation(1, 5, 6) #output: " The solution are x1=(-2-0j) and x2=(-3+0j)"
# solve_quadric_equation(0, 8, 1) #output: "Zero Division Error"
# solve_quadric_equation(1,"abc", 5) #output: "Could not convert string to float"
