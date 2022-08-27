# 1. У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен його відгадати не більше ніж за 10 спроб.
#     Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
#     Якщо за 10 спроб число не відгадане, то вивести загадане число.

from random import randint

n = randint(0, 100)
print(n)
m = 0
while m <= 10:
    if m == 10:
        print(f"You failed! \n n = {n}")
        break
    print(f"Your try number: {m + 1}")
    d = int(input("\tEnter your number: "))
    if n == d:
        print("You win!")
        break
    else:
        if n > d:
            print("Your number is less then n")
        else:
            print("Your number is bigger then n")
    m += 1
# 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)
i = 0
n = 0
while i < 10:
    d = int(input(f"Enter number your {i + 1} (bigger then 2):"))
    if d > 2 and d % 5 == 0:
        n += 1
    elif d <= 2:
        print("     wrong! The number is less or equal 2")
    i += 1
print(f"Numbers that are multiple of 5: {n}")

# 3. Вивести на екран таблицю множення (від 1 до 9).
i = 1
j = 1
while i <= 9:
    print(i)
    while j < 10:
        print(f"\t{i} X {j} = {i * j}")
        j += 1
    j = 1
    i += 1

# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
#     Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

N = int(input("Enter height: "))
M = int(input("Enter width: "))
for i in range(N):
    print("")
    for j in range(M):
        if j == 0 or j == M - 1 or i == 0 or i == N - 1:
            print('#', end='')
        else:
            print("/", end='')

# 5. Дано число P  і число H. Користувач вводить послідовність чисел. Визначити: суму тих чисел, які менше P;
#     добуток чисел, які більші за H; кількість чисел, що знаходяться  в діапазоні значень від P до H.
#     При введенні числа рівного P або H, припинити обчислення та вивести результат. (не використовувати білдін функції)
P = 20
H = 50
sum = 0
mul = 1
kol = 0
print(f"P = {P}\nH = {H}")
while True:
    num = int(input("Enter your number:"))
    if num < P:
        sum = sum + num
    elif num > H:
        mul = mul * num
    elif P < num < H:
        kol += 1
    else:
        break
    print(f"Sum = {sum}; Dobutok = {mul}; Kol = {kol}")

# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. При введенні числа 0 закінчити роботу.
sum_of_num = 0
positive = 0
negative = 0
while True:
    num = int(input("Enter your number: "))
    if num > 0:
        sum_of_num += 1
        positive += 1
    elif num < 0:
        sum_of_num += 1
        negative += 1
    else:
        break
print(f"Percent of negative numbers: {negative / sum_of_num * 100}%")
print(f"Percent of positive numbers: {positive / sum_of_num * 100}%")
