import math
print("Task 1")

while True:
    year = int(input("Year ="))
    if year > 0:
        break
    else:
        print("Our program can only operate with years AD, sorry for inconvenience")
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year!")
else:
    print("This is not a leap year!")


print("Task 2")

year = int(input("Year ="))
month = int(input("Month ="))
day = int(input("Day ="))
if year > 0:
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 < day <= 31:
        print('Correct')
    elif month in [4, 6, 9, 11] and 1 < day <= 30:
        print('Correct')
    elif month == 2 and (1 < day <= 28):
        print('Correct')
    elif (
            year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and month == 2 and day == 29:
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')

date = "{d}.{m}.{y}".format(d=day, m=month, y=year)
print(date)


print("Task 3")

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = b ** 2 - 4 * a * c
print(d)
x1 = None
x2 = None
if d == 0:
    x1, x2 = (-b + math.sqrt(d)) / (2 * a)
    print("x =", x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
else:
    print('No square root')
if x1 and x2:
    print("x1 =", x1, "\nx2 =", x2)


print("Task 4")

a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
if (a + b) > c and (b + c) > a and (a + c) > b:
    perimeter = a + b + c
    p_half = perimeter / 2
    s = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
    print("Perimeter = ", perimeter)
    print("Area of triangle = ", s)
else:
    print("Wrong triangle")


print("Task 5")

print("Please, enter a day of the year.")
while True:
    k = int(input("Day of the year ="))
    if 1 <= k <= 365:
        break
    elif k == 366:
        print("Our program can only handle non-leap years right now. Sorry for inconvenience.")
    else:
        print("This is not a day of a non-leap year.")
day_in_week = k % 7
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
print("Day of the week is", n)

input()
