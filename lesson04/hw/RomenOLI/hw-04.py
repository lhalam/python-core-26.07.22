#Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні
year = int(input("please, input year - "))
if year % 4 == 0:
    if year % 100 != 0:
        print("It's a leap year!")
    else:
        if year % 400 == 0:
            print("It's a leap year!")
        else:
            print("This is not a leap year!")
else:
    print("This is not a leap year!")