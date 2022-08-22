"1. Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними. Якщо третій аргумент +,"
'додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок "Невідома операція".'

def arithmetic(a, b, operation):
    match operation:
        case '-':
            return a - b
        case '+':
            return a + b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            return "Невідома операція"

# print(arithmetic(int(input('a = ')), int(input('b = ')), input('operation = ')))

'2. Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і `False` в іншому випадку.'

def is_year_leap(year):
    return not year % 4

# print(is_year_leap(int(input('Enter year: '))))

'3. Написати функцію `square`, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.'

def square(length):
    return length * 4, length**2, (length**2 + length**2)**0.5

# print(square(int(input('Enter side length of a square: '))))

'4. Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).'

def season(num):
    match num:
        case 12 | 1 | 2:
            return 'Winter'
        case 3 | 4 | 5:
            return 'Spring'
        case 6 | 7 | 8:
            return 'Summer'
        case 9 | 10 | 11:
            return 'Autumn'

# print(season(int(input('Enter month number: '))))

'5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).'
'Написати функцію `bank`, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.'

def bank(uah, years):
    for years in range(years):
        uah += uah * 0.1
    return str(uah) + ' UAH'

# print(bank(int(input('How many UAH? \n')), int(input('How many years? \n'))))

'6. Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і `False` - в іншому випадку.'

def is_prime(num):
    count = 0
    for n in range(1, num + 1):
        if not num % n:
            count += 1
    return count == 2

# print(is_prime(int(input('Enter num: '))))

'7. Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і `False` - в іншому випадку.'

def date(day, month, year):
    if 0 < year <= 2022 or 1 <= month <= 12 or 1 <= day <= 31:
        if month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32):
            return True
        elif month == 2 and (year % 4 == 0 and day in range(1, 30)) or \
                            (year % 4 in (1, 2, 3) and day in range(1, 29)):
            return True
        elif month in (4, 6, 9, 11) and day in range(1, 31):
            return True
        else:
            return False
    else:
        return False

# print(date(int(input('Enter day: ')), int(input('Enter month: ')), int(input('Enter year: '))))