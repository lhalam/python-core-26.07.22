# ''' • Ввести значення(рік), вивести повідомлення "It's a leap year!" якщо рік
#   високосний і "This is not a leap year!" якщо ні.'''

match int(input()):
    case 365:
        print("This is not a leap year!")
    case 366:
        print("It's a leap year!")
    case _:
        print('Wrong number of days entered')

# '''  • Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити
#   чи введені дані відповідають коректному запису дати.'''

year, month, day = int(input()), int(input()), int(input())

if 0 < year <= 2022:
    if 1 <= month <= 12:
        if 1 <= day <= 31:
            if month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32):
                print('👍')
            elif month == 2 and (year % 4 == 0 and day in range(1, 30)) or (year % 4 in (1, 2, 3) and day in range(1, 29)):
                print('👍')
            elif month in (4, 6, 9, 11) and day in range(1, 31):
                print('👍')
            else:
                print('👎')
        else:
            print('Wrong day entered')
    else:
        print('Wrong month entered')
else:
    print('Wrong year entered')

# '''  • Для довільних дійсних чисел a, b, і c визначити, чи має рівняння
#   ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.'''

a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))

D = b**2 - 4*a*c
print('Discriminant =', D)
if D > 0:
    x1 = (-b + D*0.5) / (2 * a)
    x2 = (-b - D*0.5) / (2 * a)
    print(f'Roots: {int(x1)}, {int(x2)}')
elif D == 0:
    print('Root:', int(-b / (2 * a)))
else:
    print('No roots')

# '''  • Задано три довільних числа. Визначити, чи можна побудувати
#   трикутник з такими довжинами сторін; Якщо так, то видрукувати його
#   периметр та площу.'''

a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))

if a + b > c and b + c > a and a + c > b:
    p = a + b + c
    print('\033[1mPerimeter\033[0m of a trigon =', p)
    print('\033[1mArea\033[0m of a trigon = ', (p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c))**0.5)
else:
    print("Wrong trigon")

# '''   • Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення
# (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який
# день тижня припадає k-й день не високосного року, в якому 1 січня -
# понеділок'''

def day_of_week(day_num):
    while day_num not in range(1, 366):
        return day_of_week(int(input('Wrong number of days, please enter a valid number: ')))
    day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 0: 'Sunday'}
    return f'The day number ({day_num}) you entered means this day of the week - {day[day_num % 7]}'

print(day_of_week(int(input('Enter a day number between 1 and 365: '))))