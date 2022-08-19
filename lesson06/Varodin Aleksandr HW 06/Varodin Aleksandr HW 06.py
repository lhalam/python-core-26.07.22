# Task 1

import random

random_list = []
user_list = []
result = []
count = 0
while count != 5:
    user_list.append(int(input()))
    random_list.append(random.randint(0 , 100))
    count += 1
print(user_list)
print(random_list)
for index , i in enumerate(random_list):
    sum = i + user_list[index]
    result.append(sum)
print(result)

# Task 2

user_list = []
count = 0
sum = 0
umnozheniye = 1
while count != 5:
    user_list.append(int(input()))
    count += 1
print(user_list)
for i in user_list:
    sum += i
    umnozheniye *= i
print(sum)
print(umnozheniye)

# Task 3

import random

user_list = []
count_plus = 0
count_minus = 0
count_zero = 0
count = 0
while count != 20:
    user_list.append(random.randint(-5, 4))
    count += 1
print(user_list)
for i in user_list:
    if i == 0:
        count_zero += 1
    if i < 0:
        count_minus += 1
    if i > 0:
        count_plus += 1
print(count_plus)
print(count_minus)
print(count_zero)

# Task 4

import random

user_list = []
count_plus = []
count_minus = []
count = 0
while count != 11:
     user_list.append(random.randint(-5, 5))
     count += 1
print(user_list)
for i in user_list:
    if i > 0:
        count_plus.append(i)
    if i < 0:
        count_minus.append(i)
print(count_plus)
print(count_minus)

#Task 5

import random


user_list = []
count = 0
while count != 11:
     user_list.append(random.randint(-5, 5))
     count += 1
print(user_list)
for i in user_list:
    if i < 0:
        user_list.remove(i)
print(user_list)

# Task 6

numbers = [1, 3, 8, 9, 7, 4, 5, 9, 12]
index_list = []
for index, i in enumerate(numbers):
    if i % 2 == 0:
        index_list.append(index)
print(index_list)

# Task 7

list_1 = [1, 5, 1, 5, 8, 7, 12, 2, 2]
new_list = list(set(list_1))
print(new_list)

# Task 8

import random
list_1 =[]
count = 0
minim = 0
maxim = 0
while count != 10:
    list_1.append(random.randint(0, 10))
    count += 1
print(list_1)
min_value = min(list_1)
min_index = list_1.index(min_value)
max_value = max(list_1)
max_index = list_1.index(max_value)
list_1[min_index], list_1[max_index] = list_1[max_index], list_1[min_index]
print(list_1)

# Task 9

list_1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
result = []
for i in list_1:
    sum_1 = 0
    for j in i:
        sum_1 += j
    i.append(sum_1)
list_2 = list(zip(*list_1))
for i in list_2:
    sum_1 = 0
    for j in i:
        sum_1 += j
    result.append(sum_1)
list_1.append(result)
print(list_1)

# Task 10

import random
matrix_1 = []
count_1 = 0
count_2 = 0
internal_matrix = []
count_double = 0
while count_1 != 4:
    count_1 += 1
    while count_2 != 4:
        internal_matrix.append(random.randint(0, 999))
        count_2 += 1
    matrix_1.append(internal_matrix)
    count_2 = 0
    internal_matrix = []
print(matrix_1)
for i in matrix_1:
    for j in i:
        if 10 <= j <= 99:
            count_double += 1
print(count_double)

# Task 11

numbers_1 = []
numbers_2 = []
count_1 = 0
count_2 = 0
sum_1 = 0
while count_1 != 4:
    count_1 += 1
    while count_2 != 4:
        count_2 += 1
        numbers_2.append(int(input()))
    numbers_1.append(numbers_2)
    count_2 = 0
    numbers_2 = []
print(numbers_1)
for i in numbers_1:
    for j in i:
        sum_1 += j
    i.append(sum_1)
    sum_1 = 0
print(numbers_1)

# Task 12

import random
matrix_1 = []
count_1 = 0
count_2 = 0
internal_matrix = []
count_double = 0
while count_1 != 4:
    count_1 += 1
    while count_2 != 4:
        internal_matrix.append(random.randint(0, 999))
        count_2 += 1
    matrix_1.append(internal_matrix)
    count_2 = 0
    internal_matrix = []
print(matrix_1)
new_matrix = list(zip(*matrix_1))
print(new_matrix)
minimal_list = []
maximum_number = None
for i in new_matrix:
    minimal_list.append(min(i))
print(minimal_list)
maximum_number = max(minimal_list)
print(maximum_number)

# Task 13

import random
matrix_1 = []
count_1 = 0
count_2 = 0
internal_matrix = []
count_double = 0

matrix_2 = []
count_1_1 = 0
count_2_2 = 0
internal_matrix_1 = []
count_double_1 = 0
while count_1 != 2:
    count_1 += 1
    while count_2 != 2:
        internal_matrix.append(int(input()))
        count_2 += 1
    matrix_1.append(internal_matrix)
    count_2 = 0
    internal_matrix = []
print(matrix_1)
while count_1_1 != 2:
    count_1_1 += 1
    while count_2_2 != 2:
        internal_matrix_1.append(int(input()))

        count_2_2 += 1
    matrix_2.append(internal_matrix_1)
    count_2_2 = 0
    internal_matrix_1 = []
print(matrix_2)
result_list = []
result_list_inner = []
for index_i, i in enumerate(matrix_1):
    for index_j, j in enumerate(i):
        if j > matrix_2[index_i][index_j]:
            result_list_inner.append(j)
        else:
            result_list_inner.append(matrix_2[index_i][index_j])
    result_list.append(result_list_inner)
    result_list_inner = []
print(result_list)

# Task 14

import random
matrix_1 = []
count_1 = 0
count_2 = 0
internal_matrix = []
while count_1 != 10:
    count_1 += 1
    while count_2 != 10:
        internal_matrix.append(random.randint(0, 999))
        count_2 += 1
    matrix_1.append(internal_matrix)
    count_2 = 0
    internal_matrix = []
print(matrix_1)
main_index = 0
second_index = len(matrix_1[0]) - 1
for i in range(len(matrix_1[0])):
    matrix_1[i][main_index], matrix_1[i][second_index] = matrix_1[i][second_index], matrix_1[i][main_index]
    main_index += 1
    second_index -= 1
print(matrix_1)


