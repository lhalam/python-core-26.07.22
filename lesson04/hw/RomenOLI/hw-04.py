#Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні

def is_lipyear(year):
    text = ""
    if year % 4 == 0:
        if year % 100 != 0:
            text = "It's a leap year!"
        else:
            if year % 400 == 0:
                text = "It's a leap year!"
            else:
                text = "This is not a leap year!"
    else:
        text = "This is not a leap year!"
    return text

# print(is_lipyear(int(input("please, input year - "))))

#Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати
year, month, day = int(input("input year  - ")), int(input("input month  - ")), int(input("input day  - "))

if month in (1, 3, 5, 7, 8, 10, 12) and day == 31:
    print("It is correct")
elif month in (4, 6, 8, 11) and day == 30:
    print("It is correct")
elif month == 2:
    if is_lipyear(year) == "It's a leap year!" and day == 29:
        print("It is correct")
    else:
        print("It is not correct")
else:
    print("It is not correct")