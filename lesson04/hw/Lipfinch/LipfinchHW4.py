# 1) Вести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний та "It's not a leap year!", якщо рік ні

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} It's a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} It's a leap year!".format(year))

else:
    print("{0} It's not a leap year".format(year))

# 2) Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити
#   чи введені дані відповідають коректному запису дати.

year = int(input())
month = int(input())
day = int(input())











