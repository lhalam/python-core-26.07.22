from datetime import (datetime,
                      date,
                      tzinfo)

s = ("Beautiful is better than ugly."
     "Explicit is better than implicit."
     "Simple is better than complex.")
print(s)


def is_lipyear(year):
    return "It's a leap year!" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "This is not a leap year!"


# year, month, day = int(input("input year  - ")), int(input("input month  - ")), int(input("input day  - "))
year, month, day = int(input("input year  - ")), int(input("input month  - ")), int(input("input day  - "))
if month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
    print("It is correct date")
elif month in (4, 6, 8, 11) and day <= 30:
    print("It is correct date")
elif month == 2:
    if ((is_lipyear(year) == "It's a leap year!" and day <= 29) or
            (is_lipyear(year) != "It's a leap year!" and day <= 28)):
        print("It is correct date")
    else:
        print("It is not correct date")
else:
    print("It is not correct date")
