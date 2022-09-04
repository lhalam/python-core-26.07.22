# # Task 1
#
# def valid_email(email):
#     try:
#         a = email.split('@')
#         if len(a) == 2 and a[1] == 'ukr.tel.com':
#             return "Email is valid"
#         else:
#             return "Email is not valid"
#     except AttributeError:
#         return "Email is not valid"
#
# print(valid_email('trafik@ukr.tel.com'))
# #
# # Task 2
#
# def day_of_week(day):
#     days = {1:'monday',2:'tuesday',3:'wednrsday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
#     try:
#         return days[day]
#     except Exception:
#         if isinstance(day, int):
#             return "There is no such day of the week! Please try again."
#         if isinstance(day, str):
#             return "You did not enter a number! Please try again."
# print(day_of_week(5))
#
# # Task 3
#
# def check_odd_even(number):
#     try:
#         if number % 2 == 0:
#             return "Entered number is even"
#         if number % 2 != 0:
#             return "Entered number is odd"
#     except TypeError:
#         return "You entered not a number."
# print(check_odd_even("monday"))
#
# # Task 4

# def divide(numerator, denominator):
#     try:
#         result = numerator/denominator
#         return f'Result is {result}'
#     except ZeroDivisionError:
#         return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
#     except TypeError:
#         return "Value Error! You did not enter a number!"
#     # except Exception as e:
#     #     print(e.__class__)
# print(divide('10',2))

# Task 5

# class ToSmallNumberGroupError(BaseException):
#     def __init__(self, text):
#         self.error_text = text
#
#     def __str__(self):
#         return self.error_text
#
# def check_number_group(number):
#     try:
#         if number > 10:
#             return "Number of your group input parameter of function is valid"
#         if number <= 10:
#             raise ToSmallNumberGroupError("We obtain error: Number of your group can't be less than 10")
#     except TypeError:
#         return "You entered incorrect data."
# print(check_number_group(9))

# Task 6

# class MyError(BaseException):
#     def __init__(self, text):
#         self.error_text = text
#
#     def __str__(self):
#         return self.error_text
#
# def check_positive(number):
#     try:
#         if number > 0:
#             return f'You input positive number: {number}'
#         if number < 0:
#             raise MyError(f'You input negative number: {number}. Try again.')
#     except TypeError:
#         return "Error type: ValueError!"
# print(check_positive(1))

# Task 7














