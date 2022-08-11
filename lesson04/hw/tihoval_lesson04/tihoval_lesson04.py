
# task1


year = int(input('Enter year: '))

if not year % 4:
    print("It's a leap year!")
else:
    print("This is not a leap year!")

# task2

import datetime
import math

year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

try:
    print(datetime.datetime(year, month, day))
except ValueError:
    print("Not valid values")

# task3

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = b ** 2 - 4 * a * c

if d < 0:
    print("Has no roots")
elif d == 0:
    print("x = ", -b / 2 * a)
else:
    print("x1 = ", (-b - math.sqrt(d)) / 2 * a, "\nx2 = ", (-b + math.sqrt(d)) / 2 * a)

# task4

triangle = [0, 0, 0]
triangle[0] = int(input('a: '))
triangle[1] = int(input('b: '))
triangle[2] = int(input('c: '))

triangle.sort()
p = sum(triangle) / 2
if triangle[2] < triangle[0] + triangle[1]:
    print("P = ", 2 * p, "\nS = ", math.sqrt(p * (p - triangle[0]) * (p - triangle[1]) * (p - triangle[2])))
else:
    print("Not triangle")

# task5

day = int(input('day: '))

match day % 7:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 0:
        print("Sunday")


