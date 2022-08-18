import math
from random import randint


def print_list(ar):
    for i in ar:
        print(*i)


# Task1
rand_list = [randint(1, 100) for i in range(5)]
user_list = [int(input(f"input element {j + 1} -")) for j in range(5)]
result_list = [rand_list[i] + user_list[i] for i in range(5)]
print(user_list)
print(rand_list)
print(result_list)

# Task2
user_list = [int(input(f"input element {j + 1} -")) for j in range(5)]
print(f"Sum elem = {sum(user_list)}")
print(f"Dob elem = {math.prod(user_list)}")

# Task3
rand_list = [randint(-5, 4) for i in range(20)]
print_list(rand_list)
print(f"Null elements {sum(map(lambda x: x == 0, rand_list))}")
print(f"Neg elements {sum(map(lambda x: x < 0, rand_list))}")
print(f"Pos elements {sum(map(lambda x: x == 0, rand_list))}")

# Task4
rand_list = [i for i in range(-5, 5)]
neg_list = [j for j in rand_list if j < 0]
pos_list = [j for j in rand_list if j > 0]
print(f"Null mass {pos_list}")
print(f"Neg mass {neg_list}")
print(f"Gen mass {rand_list}")

# Task5
rand_list = [randint(-10, 20) for i in range(20)]
print_list(rand_list)
k = list(filter(lambda x: x > 0, rand_list))
print(k)

# Task6
rand_list = [randint(-10, 20) for j in range(20)]
print_list(rand_list)
print([rand_list.index(i) for i in rand_list if i % 2 == 0])

# Task7
rand_list = [randint(-10, 20) for i in range(20)]
print(rand_list)
print([i for i in rand_list if (rand_list.count(i) == 1)])

# Task8
rand_list = [randint(-10, 20) for i in range(5)]
print(rand_list)
print(min(rand_list))
print(max(rand_list))
max_ind = rand_list.index(max(rand_list))
min_ind = rand_list.index(min(rand_list))
rand_list[max_ind], rand_list[min_ind] = rand_list[min_ind], rand_list[max_ind]
print_list(rand_list)

# Task9
matrix_len = 10
rand_list = [[randint(1, 11) for j in range(matrix_len)] for i in range(matrix_len)]
for i in range(matrix_len):
    rand_list[i].append((sum(rand_list[i])))
rand_list.insert((len(rand_list)), ([sum(x) for x in zip(*rand_list)]))
print_list(rand_list)

# Task10
matrix_len = 5
rand_list = [[randint(0, 999) for j in range(matrix_len)] for i in range(matrix_len)]
kol_two_digits = 0
for i in range(matrix_len):
    for j in range(matrix_len):
        if 9 < rand_list[i][j] < 100:
            kol_two_digits += 1
print(kol_two_digits)

# Task11
rand_list = [[1] * 5 for _ in range(3)]
for i in range(3):
    for k in range(5):
        rand_list[i][k] = int(input('Input num: '))
rand_list.insert((len(rand_list)), ([sum(x) for x in zip(*rand_list)]))
print_list(rand_list)

# Task12
rand_list = [[randint(1, 11) for j in range(matrix_len)] for i in range(matrix_len)]
min_elem = [min(i) for i in rand_list]
print(max(min_elem))

# Task13
matrix_len = 2
rand_list = [[1] * matrix_len for _ in range(2)]
rand_two = [[1] * matrix_len for _ in range(2)]
res_matrix = [[1] * matrix_len for _ in range(2)]
for i in range(matrix_len):
    for k in range(matrix_len):
        rand_list[i][k] = int(input('Input num: '))
        rand_two[i][k] = int(input('Input num matrix two: '))
        res_matrix[i].append(rand_list[i][k] if rand_list[i][k] >= rand_two[i][k] else rand_two[i][k])
print_list(res_matrix)

# Task14
matrix_len = 10
rand_list = [[randint(1, 40) for j in range(matrix_len)] for i in range(matrix_len)]
print_list(rand_list)
for i in range(matrix_len):
    k = len(rand_list) - 1 - i
    rand_list[i][i], rand_list[i][k] = rand_list[i][k], rand_list[i][i]
print_list(rand_list)

# Task15
matrix_len = 5
rand_list = [[randint(1, 40) for j in range(matrix_len)] for i in range(matrix_len)]
kol = matrix_len - 1
print()
print_list(rand_list)
while kol > 0:
    id_elem = 0
    for j in range(kol + 1):
        if rand_list[0][j] > rand_list[0][id_elem]:
            id_elem = j
    for i in range(matrix_len):
        m = rand_list[i][id_elem]
        rand_list[i][id_elem] = rand_list[i][kol]
        rand_list[i][kol] = m
    kol -= 1
print_list(rand_list)
