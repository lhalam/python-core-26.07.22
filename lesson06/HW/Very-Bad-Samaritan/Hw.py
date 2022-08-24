import random

print("Task 1")

random_list = [random.randint(-30, 30) for _ in range(10)]
user_list = [int(input("Enter number >>> ")) for _ in range(10)]
sum_elements = [random_list[i] + user_list[i] for i in range(len(random_list))]
print(f'Random list: {random_list}\n'
      f'User input list: {user_list}\n'
      f'Sum = {sum_elements}')


print("Task 2")

user_list, sum_, mult = [], 0, 1
for i in range(10):
    user_input = int(input("Enter number >>> "))
    user_list.append(user_input)
    sum_ += user_input
    mult *= user_input
print(f"{user_list}\nSum: {sum_}\nMultiple: {mult}")


print("Task 3")

random_list = [random.randint(-5, 4) for _ in range(20)]
negative = len(list(filter(lambda x: x < 0, random_list)))
positive = len(list(filter(lambda x: x > 0, random_list)))
zero = len(list(filter(lambda x: x == 0, random_list)))
print(f'{random_list}\nNegative numbers = {negative}\n'
      f'Positive numbers = {positive}\nZeros = {zero}')


print("Task 4")

numbers_list = []
negative = []
positive = []
for _ in range(10):
    random_num = random.randint(-5, 5)
    numbers_list.append(random_num)
    if random_num > 0:
        positive.append(random_num)
    elif random_num < 0:
        negative.append(random_num)
print(f"{numbers_list}\nPositive numbers = {positive}\nNegative numbers = {negative}")


print("Task 5")

random_list = [random.randint(-5, 5) for _ in range(40)]
print(random_list)
negative = [num for num in random_list if num < 0]
for num in negative:
    random_list.remove(num)
print(random_list)


print("Task 6")

random_list = [random.randint(1, 30) for _ in range(25)]
print(random_list)
index_list = [i for i in range(len(random_list)) if random_list[i] % 2 == 0]
print(index_list)


print("Task 7")

random_list = [random.randint(-30, 30) for _ in range(20)]
print(random_list)
for el in random_list:
    if random_list.count(el) == 1:
        print(el, end=' ')


print("Task 8")

random_list = [random.randint(1, 100) for _ in range(10)]
print(random_list)
max_num, max_index = max(random_list), random_list.index(max(random_list))
min_num, min_index = min(random_list), random_list.index(min(random_list))
random_list.remove(min_num)
random_list.remove(max_num)
random_list.insert(max_index, min_num)
random_list.insert(min_index, max_num)
print(random_list)


print("Task 9")

matrix = [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]
new_line = []

for i in range(len(matrix)):
    sum_rows = 0
    sum_col = 0
    for j in range(len(matrix[i])):
        sum_rows += matrix[i][j]
        sum_col += matrix[j][i]
    matrix[i].append(sum_rows)
    new_line.append(sum_col)
matrix.append(new_line)
for i in matrix:
    print(i)


print("Task 10")

matrix = [[random.randint(0, 999) for _ in range(10)]for _ in range(10)]
for i in matrix:
    print(i)
count = 0
for m in matrix:
    for num in m:
        if len(str(num)) == 2:
            count += 1
print(count)


print("Task 11")

matrix = [[int(input("Enter number >>> ")) for _ in range(4)]for _ in range(4)]
for i in range(len(matrix)):
    matrix[i].append(sum(matrix[i]))
for i in matrix:
    print(i)


print("Task 12")

matrix = [[random.randint(-9, 9) for _ in range(5)]for _ in range(5)]
for i in matrix:
    print(i)
l_min = [min(i) for i in matrix]
print(max(l_min))


print("Task 13")

n = 5  # Matrix size
matrix_1 = [[int(input("Enter num for matrix-1 >>> ")) for _ in range(n)]for _ in range(n)]
matrix_2 = [[int(input("Enter num for matrix-2 >>> ")) for _ in range(n)]for _ in range(n)]
matrix_3 = [['_'] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        matrix_3[row][col] = matrix_1[row][col] if matrix_1[row][col] >= matrix_2[row][col] else matrix_2[row][col]
for i in matrix_1:
    print(i)
print()
for i in matrix_2:
    print(i)
print()
for i in matrix_3:
    print(i)


print("Task 14")

n = 10
matrix = [[b * a for b in range(1, n + 1)] for a in range(1, n + 1)]
print('Before:')
for row in range(n):
    for col in range(n):
        print(str(matrix[row][col]).ljust(2), end=' ')
    print()

for i in range(n):
    matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]

print('After:')
for row in range(n):
    for col in range(n):
        print(str(matrix[row][col]).ljust(2), end=' ')
    print()


print("Task 15")

n = 7
matrix = [[random.randint(-9, 9) for _ in range(n)]for _ in range(n)]
print('Before')
for i in range(n):
    for j in range(n):
        print("{:4d}".format(matrix[i][j]), end='')
    print()

print('After')
k = n-1
while k > 0:
    ind = 0
    for j in range(k+1):
        if matrix[0][j] > matrix[0][ind]:
            ind = j
    for i in range(n):
        m = matrix[i][ind]
        matrix[i][ind] = matrix[i][k]
        matrix[i][k] = m
    k -= 1

for i in range(n):
    for j in range(n):
        print("{:4d}".format(matrix[i][j]), end='')
    print()
