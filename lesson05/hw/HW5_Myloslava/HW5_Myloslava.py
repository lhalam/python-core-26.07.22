#task 1  У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен його відгадати
# не більше ніж за 10 спроб. Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене
# користувачем число, ніж те, що загадане. Якщо за 10 спроб число не відгадане, то вивести загадане число.
#
# import random
# n = random.randint(0, 100)
# print(n)
#
# att = 0
# while att <= 10:
#     number = int(input())
#     if n > number:
#         att += 1
#         print("The random number is bigger")
#     elif n < number:
#         att += 1
#         print("The random is smaller")
#     elif n == number:
#         att = 10
#         print("Winner")

# task 2
#Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)

# a = 0
# while a != 10:
#     i = int(input())
#     if i % 5 == 0:
#         print(a)
#     a += 1

# task 3 Вивести на екран таблицю множення (від 1 до 9).
#
num_1 = 1
while num_1 <= 9:
    num_2 = 1
    while num_2 <= num_1:
        print(num_1, "*", num_2, "=", num_1*num_2, end='\t' )
        num_2 +=1
    print()
    num_1 +=1

# task 4 Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
# Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

for i in range(10):
    if i==0 or i==9:
        for j in range(15):
            print('*',end='')
    else:
        print('*',end='')
        for j in range(1,14):
            print('o',end='')
        print('*',end='')
    print()

#task 5 Дано число P і число H. Користувач вводить послідовність чисел.
# Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H ;
# кількість чисел, що знаходяться в діапазоні значень від P до H . При введенні числа рівного P або H,
# припинити обчислення та вивести результат. (не використовувати білдін функції)
p = 5
h = 7
users_input = input()
list_number = users_input.split()
sum_less_p = 0
increase = 1
count = 0
for i in list_number:
    if p == int(i) or h == int(i):
        break
    if int(i) < p:
        sum_less_p += int(i)
    if int(i) > h:
        increase = increase * int(i)
    if p < int(i) < h:
        count += 1
print(sum_less_p, increase, count)

# task 6 Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел.
# При введенні числа 0 закінчити роботу.

count_plus = 0
count_minus = 0
count_total = 0
number = 1
while number != 0:
    number = int(input())
    if number == 0:
        percent_positive = count_plus * 100 / count_total
        percent_negative = count_minus * 100 / count_total
        break
    count_total += 1
    if number >= 0:
        count_plus += 1
    elif number < 0:
        count_minus += 1
print(percent_negative, percent_positive)