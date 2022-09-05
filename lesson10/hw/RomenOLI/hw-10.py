#1. CheckEmail
# def valid_email(email):
#     try:
#         if email.count("@") == 0 or email.count("@") > 1:
#             raise ValueError("@ error")
#         personal_info = email[:email.find("@")]
#         if len(personal_info) == 0:
#             raise ValueError("personal info error")
#         domain_info = email[email.find("@")+1:]
#         if len(domain_info) == 0:
#             raise ValueError("domain info error")
#         if "_" in domain_info:
#             raise ValueError("domain info error")
#         if domain_info[-1] == "." or domain_info.find("..") != -1:
#             raise ValueError("domain info error")
#         dom = domain_info[::-1]
#         if not dom[:dom.find(".")].isalpha():
#             raise ValueError("domain error")
#     except ValueError as err:
#         print("Email is not valid - ", err)
#     else:
#         print("Email is valid")
#
# valid_email(input("input email - "))

# 2. DayOfWeek

# def day_of_week(day_n):
#     try:
#         if not day_n.isnumeric():
#             raise TypeError("It is incorrect type!")
#         if int(day_n) not in range(1,8):
#             raise ValueError("not in range!")
#     except ValueError as err:
#         print("There is no such day of the week! Please try again. - ", err)
#     except TypeError as err:
#         print("There is no such day of the week! Please try again. - ", err)
#     else:
#         match int(day_n):
#             case 1:
#                 print("Monday")
#             case 2:
#                 print("Tuesday")
#             case 3:
#                 print("Wednesday")
#             case 4:
#                 print("Thursday")
#             case 5:
#                 print("Friday")
#             case 6:
#                 print("Saturday")
#             case 7:
#                 print("Sunday")
#
# day_of_week(input("input number of day in a week - "))

# 3. EvenOddNUmber

# def check_odd_even(numb):
#     try:
#         if not numb.isnumeric():
#             raise TypeError("incorrect type!")
#     except TypeError as err:
#         print("You entered not a number.")
#     else:
#         print("Entered number is even" if int(numb) % 2 == 0 else "Entered number is odd")
#
# check_odd_even(input("input number - "))

# 4. DivideNumber
# def divide(numerator, denominator):
#     try:
#         if not numerator.isnumeric() or not denominator.isnumeric():
#             raise ValueError("Value Error! You did not enter a number!")
#         if denominator == '0':
#             raise ZeroDivisionError(f"Oops, {numerator} / 0 denominator, division by zero is error!!!")
#     except ValueError as err:
#         print("Valur Error! ", err)
#     except ZeroDivisionError as err:
#         print(err)
#     else:
#         print(f"Result is {int(numerator)/int(denominator)}")
#
# divide(input("input numerator - "), input("input denominator - "))

# 5. NumberOfGroup
# class ToSmallNumberGroupError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# def check_number_group(number):
#     try:
#         if not number.isnumeric():
#             raise TypeError("You entered incorrect data. Please try again.")
#         if int(number) <= 10:
#             raise ToSmallNumberGroupError("Number of your group can't be less than 10")
#     except TypeError as err:
#         print(err)
#     except ToSmallNumberGroupError as err:
#         print("We obtain error: ", err)
#     else:
#         print(f"Number of your group {int(number)} is valid")
#
# check_number_group(input("input your number - "))

# 6. PositiveNumber
# class MyError(ArithmeticError):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# def check_positive(number):
#     try:
#         if number.isalpha():
#             raise ValueError("Error type: ValueError!")
#         if int(number) < 0:
#             raise MyError(f"You input negative number: {number}. Try again.")
#     except MyError as err:
#         print(err)
#     except ValueError as err:
#         print(err)
#     else:
#         print(f"You input positive number: {number}")
#
# check_positive(input("input number - "))

# 7. Equation
def solve_quadric_equation(a, b, c):
    from math import sqrt
    try:
        if a.isalpha() or b.isalpha() or c.isalpha():
            raise TypeError("Could not convert string to float")
        if int(a) == 0:
            raise ZeroDivisionError("Zero Division Error")
        d = int(b)**2 - 4 * int(a) * int(c)
        x1 = (-int(b) + sqrt(d))/2*int(a)
        x2 = (-int(b) - sqrt(d))/2*int(a)
        print(f"The solution are x1=({x1}) and x2=({x2})")
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print("Math error - ", err)
    except TypeError as err:
        print(err)

solve_quadric_equation(input("input a - "), input("input b - "), input("input c - "))