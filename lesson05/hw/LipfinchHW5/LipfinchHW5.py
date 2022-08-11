# # 1. У програмі генерується випадкове ціле число від 0 до 100.
# # Користувач повинен його відгадати не більше ніж за 10 спроб.
# # Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# # Якщо за 10 спроб число не відгадане, то вивести загадане число.число

from random import randint

random_number = randint(1, 100)
number_of_attemps = 10
while number_of_attemps != 0:
    guess_number = int(input("Enter number from 1 to 100: "))
    if random_number == guess_number:
        print(f"You win, number was{guess_number}")
        break
    else:
        number_of_attemps -= 1
        print("Your number is bigger" if guess_number > random_number else "Your number is smaller")
print(f"Random number was {random_number}")

# 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)

j = 0
for i in range(10):
    num = int(input())
    if num < 2:
        print("Num must be > 2")
        continue
    else:
        if num % 5 == 0:
            j += 1
print(f'There was {j} natural numbers divisible by 5')

# 3. Вивести на екран таблицю множення (від 1 до 9).

num = int(input())
for i in range(1, 10):
   print(num, '*', i, '=', num*i)

for i in range(1,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")

# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
#    Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

sideN = int(input("Please enter first side : "))
sideM = int(input("Please enter second side  : "))
for i in range(1,sideM+1):
    for j in range(1,sideN+1):
        if i==1 or i==sideM or j==1 or j==sideN:
            print("*", end="")
        else:
            print("%", end="")
    print()

# 5.Дано число P  і число H. Користувач вводить послідовність чисел.
#   Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H;
#   кількість чисел, що знаходяться  в діапазоні значень від P до H.
#   При введенні числа рівного P або H, припинити обчислення та вивести результат. (не використовувати білдін функції)

numP = int(input("Enter number P: "))
numH = int(input("Enter number H: "))
s = 0
d = 1
k = 0
x = int(input("Enter number: "))
while x != numP and x != numH:
    if x < numP:
        s += x
    if x > numH:
        d *= x
    if x > numP and x < numH:
        k += 1
    x = int(input("Enter number: "))
print(f"Sum of numbers less then {numP} is {s}.")
print(f"Product of numbers more then {numH} is {d}.")
print(f"Amount of numbers between {numP} and {H} is {k}.")

# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. При введенні числа 0 закінчити роботу.

num = 1
x = 0
y = 0
while num != 0:
    num = int(input())
    if num > 0:
        x += 1
    y +=1
positive = x / y * 100
print(f"Positive numbers is {round(positive, 2)}%")
print(f"Negative is {round(100 - positive, 2)}%")
