#CheckEmail
class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def valid_email(mail):
    a = []
    b = []
    print(mail)
    try:
        a.append(mail.split("@"))

        if mail.count("@") != 1 or a[0][1].find("_") != -1:
            raise CustomError("Email is not valid")
        b.append(a[0][1].split("."))
        for i in range(len(b[0])):
            if not b[0][i].isalpha():
                raise CustomError("Email is not valid")

    except CustomError as e:
        print(e.data)
    else:
        print("Email is valid")
valid_email("trafik@ukr.tel.com")
valid_email("trafik@ukr_tel.com")
valid_email("tra@fik@ukr.com")
valid_email("ownsite@our.c0m")

#DayOfWeek
def day_of_week(day):
    try:
        if str(day).isnumeric():
            if  day == 1:
                print("Monday")
            elif day == 2:
                print("Tuesday")
            elif day == 3:
                print("Wednesday")
            elif day == 4:
                print("Thursday")
            elif day == 5:
                print("Friday")
            elif day == 6:
                print("Saturday")
            elif day == 7:
                print("Sunday")
            elif day < 1 or day > 7:
                raise CustomError("There is no such day of the week! Please try again.")
        else:
            raise CustomError("You did not enter a number! Please try again.")
    except CustomError as e:
        print(e.data)

day_of_week(1)
day_of_week(5)
day_of_week(50)
day_of_week("jnglkg5")

#EvenOddNumber
def check_odd_even(number):
    try:
        if  str(number).isalpha():
            raise CustomError("You entered not a number.")
        elif number%2 == 0:
            print("Entered number {number} is even")
        else:
            print("Entered number {number} is odd")

    except CustomError as e:
        print(e.data)
check_odd_even(12)
check_odd_even(13)
check_odd_even("jgjhgg")

# DivideNumber
def divide(numerator, denominator):
    try:
        if denominator == 0:
            raise CustomError(f"Oops, {numerator} / {denominator}, division by zero is error!!!")
        elif not str(denominator).isdigit() or not str(numerator).isdigit():
            raise CustomError(f"Value Error! You did not enter a number!")
        else:
            print(f"Result is {numerator/denominator}")
    except CustomError as e:
        print(e.data)

divide(12, 5)
divide(2,0)
divide("srdfg", 4)

#NumberOfGroup
class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def check_number_group(number):
    try:
        if not str(number).isdigit():
            raise CustomError("You entered incorrect data. Please try again.")
        elif int(number) < 10:
            print("Number of your group input parameter of function is valid")
        elif int(number) >= 10:
            raise ToSmallNumberGroupError("We obtain error: Number of your group can't be less than 10")

    except (ToSmallNumberGroupError, CustomError) as e:
        print(e.data)
check_number_group(4)
check_number_group(29)
check_number_group("25")
check_number_group("zxc")

#PositiveNumber
class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def check_positive(number):
    try:
        if  str(number).isalpha():
            print("Error type: ValueError!")
        elif int(number) > 0:
            print(f"You input positive number {number}: input parameter of function")
        elif number < 0:
            raise MyError(f"You input negative number {number}: input parameter of function. Try again.")
    except MyError as e:
        print(e.data)

check_positive(24)
check_positive(-19)
check_positive("38")
check_positive("abc")

#Equation
def solve_quadric_equation(a, b, c):

    try:
        if a == 0:
            print("Zero Division Error")
        elif str(a).isalpha() or str(b).isalpha() or str(c).isalpha():
            raise MyError("Could not convert string to float")
        else:
            d = b**2 - 4*a*c
            x1 = (-b + d**(0.5))/2/a
            x2 = (-b - d**(0.5))/2/a
            print(f"The solution are {x1 =} and {x2 =}")
    except  MyError as e:
        print(e.data)

solve_quadric_equation(1,5,6)
solve_quadric_equation(0,8,1)
solve_quadric_equation(1,"abc",5)


