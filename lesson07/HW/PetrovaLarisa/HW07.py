print("1. Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними."
      " Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок Невідома операція")
def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a-b
    elif c == "/":
        if b == 0:
            return "Dividing by zero"
        else:
            return a/b
    elif c == "*":
        return a*b
    else:
        return "Unknown operation"

print(arithmetic(1,2,"+"))
print(arithmetic(1,2,"-"))
print(arithmetic(1,0,"/"))
print(arithmetic(1,2,"*"))
print(arithmetic(1,2,"%"))

print("2 Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і False в іншому випадку.")
def is_year_leap(year):
    return True if year%4 == 0 and (year%100 != 0 or year%400 == 0) else False

print(is_year_leap(2300))

print("3 Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):"
      " периметр квадрата, площу квадрата і діагональ квадрата.")
def square(a):
    return f"Perimeter of a square with length of its side {a} , its area and  diagonal  are  {(4*a, a**2,2 **(0.5)*a)}"

print(square(1))
print(square(9))

print("4 Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).")
def season(number_of_month):
    if number_of_month in [3, 4, 5]:
        return "This is the spring"
    elif number_of_month in [6, 7, 8]:
        return "This is the summer"
    elif number_of_month in [9, 10, 11]:
        return "This is the autumn"
    else:
        return "This is the winter"

print(season(1))
print(season(3))
print(season(7))
print(season(10))

print("5 Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. "
      "Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки). Написати функцію bank, яка приймає аргументи n і years,"
      " і повертає суму, яка буде на рахунку користувача.")

def bank(n, years):
    sum = n
    for i in range(0, years):
        sum += 0.1*sum
    return f"In {years} years on your account will be {sum}"

print(bank(100, 1))
print(bank(100, 2))
print(bank(100, 3))
print(bank(100, 10))

print("6 Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і False - в іншому випадку.")

def is_prime(number):
    if number in range(1001):
        for i in range(2, number):
            if number%i == 0:
                return False
        return True
    else:
        return "The number must be between 0 and 1000"

print(is_prime(17))
print(is_prime(18))
print(is_prime(1000))

print("7 Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.")
def date(day, month, year):
    if month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        return True
    elif month in {4, 6, 9, 11} and day <= 30:
        return True
    elif (is_year_leap(year) and month == 2 and day <= 29) or (not is_year_leap(year) and month == 2 and day <= 28):
        return True
    else:
        return False
print(date(31, 12, 1987))
print(date(31, 2, 1987))
print(date(29, 2, 1987))
print(date(29, 2, 1984))
print(date(35, 1, 1987))

