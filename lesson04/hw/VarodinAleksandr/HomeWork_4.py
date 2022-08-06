Task 1

year = int(input())
if year == 365:
    print("It's a leap year!")
elif year == 366:
    print("This is not a leap year!")
else:
    print("Wrong number!")

# # Task 2

year = int(input())
month = int(input())
day = int(input())
if 0 < year <= 2022:
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 < day <= 31:
        print('Correct')
    elif month in [4, 6, 9, 11] and 1 < day <= 30:
        print('Correct')
    elif month == 2 and (1 < day <= 28 or day == 29):
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')

# Task 3

import math
a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
print(d)
x1 = None
x2 = None
if d == 0:
    x1, x2 = (-b + math.sqrt(d)) / (2 * a)
    print(x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
else:
    print('No square root')
if x1 != None and x2 != None:
    print(x1, x2)

# Task 4 triangle

import math
a = int(input())
b = int(input())
c = int(input())
if (a + b) > c and (b + c) > a and (a + c) > b:
    perimeter = a + b + c
    p_half = perimeter / 2
    s = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
    print(perimeter)
    print(s)
else:
    print("wrong triangle")

# # Task 5(0)

k = int(input())
day_in_week = k % 7
print(day_in_week)
if day_in_week == 1:
    n = 'monday'
elif day_in_week == 2:
    n = 'tuesday'
elif day_in_week == 3:
    n = 'wednesday'
elif day_in_week == 4:
    n = 'thursday'
elif day_in_week == 5:
    n = 'friday'
elif day_in_week == 6:
    n = 'saturday'
else:
    n = 'sunday'
print(n)

# # Task 5(1)

day_dict = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    0: 'sunday'
}
k = int(input())
day = k % 7
n = day_dict.get(day)
print(n)
