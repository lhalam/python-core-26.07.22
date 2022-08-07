year = input("Enter a year: ")
if (int(year)%400 == 0):
    print("It's a leap year!")
else:
    print("This is not a leap year!")
##########################################################################
yy = int(input("Enter year: "))
leap = False
if (yy%400 == 0):
     leap = True
mm = int(input("Enter month: "))
if not (mm > 0 and mm < 13):
     print("Month is wrong!")
else:
    dd = int(input("Enter day: "))
    if ((mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and int(dd) > 31)\
        or (leap == False and mm == 2 and dd > 28) \
        or (leap == True and mm == 2 and dd > 29) \
        or ((mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30):
        print("Data is wrong")
    else:
        print(f"You entered data: {dd}-{mm}-{yy}")
#############################################################################
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = b**2 - 4*a*c
if (D >= 0):
    x = (-b+D**(0.5))/2/a
    print("Root of the equation is: ", x)
else:
    print("The equation doesn't have real roots.")
#######################################################################
a = int(input("Enter the first side of triangle a: "))
b = int(input("Enter the second side of triangle b: "))
c = int(input("Enter the first side of triangle c: "))
if (a + b > c and a + c > b and b + c > a):
    P = a + b + c
    p = P / 2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print(f"Square of triangle S = {S}")
    print(f"Perimeter of triangle P = {P}")
else:
    print(f"It is impossible to build triangle with sides {a}, {b} and {c}")
#############################################################################
k = int(input("Enter the number of the day: "))
n = k % 7
if (n == 1):
    print(f"The {k}th day is Monday")
elif (n == 2):
    print(f"The {k}th day is Tuesday")
elif (n == 3):
    print(f"The {k}th day is Wednesday")
elif (n == 4):
    print(f"The {k}th day is Thursday")
elif (n == 5):
    print(f"The {k}th day is Friday")
elif (n == 6):
    print(f"The {k}th day is Saturday")
else:
    print(f"The {k}th day is Sunday")


