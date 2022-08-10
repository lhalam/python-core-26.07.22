# Task 1
import random

number = random.randint(0, 100)
counter_of_try = 0
while  counter_of_try <= 10:
    user_number = int(input())
    if number < user_number:
        counter_of_try += 1
        print('Число меньше рандомного')
    elif number > user_number:
        counter_of_try += 1
        print('Число больше загаданного')
    elif number == user_number:
        counter_of_try = 10
        print(number)

# Task 2

count_numbers = 0
while count_numbers != 10:
    number = int(input())
    if number % 5 == 0:
        print(count_numbers)
    count_numbers += 1

# Task 3

table = ''
for i in range(1, 10):
    for y in range(1, 10):
        table += f'{y*i}\t'
    table += f'\n'
print(table)

# Task 4

for i in range(10):
    if i==0 or i==9:
        for j in range(20):
            print('w',end='')
    else:
        print('w',end='')
        for j in range(1,19):
            print('l',end='')
        print('w',end='')
    print()

# Task 5

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

# Task 6

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
