import random

# 1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в третій
# записати суми відповідних елементів перших двох. Вивести вміст списків на екран.

# random_list = [random.randint(-30, 30) for _ in range(10)]
# user_list = [int(input("Enter number >>> ")) for _ in range(10)]
# sum_elements = [random_list[i] + user_list[i] for i in range(len(random_list))]
# print(f'Random list: {random_list}\n'
#       f'User input list: {user_list}\n'
#       f'Sum = {sum_elements}')

# 2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму
# і добуток елементів списку. Вивести на екран сам список, отримані суму і добуток його елементів.

# user_list, sum_, mult = [], 0, 1
# for i in range(10):
#     user_input = int(input("Enter number >>> "))
#     user_list.append(user_input)
#     sum_ += user_input
#     mult *= user_input
# print(f"{user_list}\nSum: {sum_}\nMultiple{mult}")

# 3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи
# списку і пораховані кількості.

# random_list = [random.randint(-5, 4) for _ in range(20)]
# negative = len(list(filter(lambda x: x < 0, random_list)))
# positive = len(list(filter(lambda x: x > 0, random_list)))
# zero = len(list(filter(lambda x: x == 0, random_list)))
# print(f'{random_list}\nNegative numbers = {negative}\n'
#       f'Positive numbers = {positive}\nZeros = {zero}')

# 4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один
# помістити тільки додатні, у другий - тільки від’ємні. Числа, рівні нулю,
# ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

# numbers_list = []
# negative = []
# positive = []
# for _ in range(10):
#     random_num = random.randint(-5, 5)
#     numbers_list.append(random_num)
#     if random_num == 0:
#         continue
#     elif random_num > 0:
#         positive.append(random_num)
#     elif random_num < 0:
#         negative.append(random_num)
# print(f"{numbers_list}\nPositive numbers = {positive}\nNegative numbers = {negative}")

# 5. Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його
# на екран. Видалити з списку всі від’ємні елементи і знову вивести.

# random_list = [random.randint(-5, 5) for _ in range(40)]
# print(random_list)
# negative = [num for num in random_list if num < 0]
# for num in negative:
#     random_list.remove(num)
# print(random_list)

# 6. У другому списку зберегти індекси парних елементів першого списку.
# Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, то другий треба
# заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля),
# оскільки саме в цих позиціях першого масиву стоять парні числа.

# random_list = [random.randint(1, 30) for _ in range(25)]
# print(random_list)
# index_list = [i for i in range(len(random_list)) if random_list[i] % 2 == 0]
# print(index_list)

# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран

# random_list = ['q', 'w', 'q']
# for el in random_list:
#     if random_list.count(el) == 1:
#         print(el, end=' ')

# 8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

# random_list = [random.randint(1, 100) for _ in range(10)]
# print(random_list)
# max_num, max_index = max(random_list), random_list.index(max(random_list))
# min_num, min_index = min(random_list), random_list.index(min(random_list))
# random_list.remove(min_num)
# random_list.remove(max_num)
# random_list.insert(max_index, min_num)
# random_list.insert(min_index, max_num)
# print(random_list)

# 9. Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем,
# який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

# matrix = [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]
# new_line = []
#
# for i in range(len(matrix)):
#     sum_rows = 0
#     sum_col = 0
#     for j in range(len(matrix[i])):
#         sum_rows += matrix[i][j]
#         sum_col += matrix[j][i]
#     matrix[i].append(sum_rows)
#     new_line.append(sum_col)
# matrix.append(new_line)
# for i in matrix:
#     print(i)

# 10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.

# matrix = [[random.randint(0, 999) for _ in range(5)]for _ in range(5)]
# for i in matrix:
#     print(i)
# count = 0
# for m in matrix:
#     for num in m:
#         if len(str(num)) == 2:
#             count += 1
# print(count)

# 11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
# Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.

# matrix = [[int(input("Enter number >>> ")) for _ in range(4)]for _ in range(4)]
# for i in range(len(matrix)):
#     matrix[i].append(sum(matrix[i]))
# for i in matrix:
#     print(i)

# 12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

# matrix = [[random.randint(-9, 9) for _ in range(5)]for _ in range(5)]
# for i in matrix:
#     print(i)
# l_min = [min(i) for i in matrix]
# print(max(l_min))

# 13. Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці
# такої ж розмірності записати більші з відповідних елементів перших двох.

# n = 5  # Matrix size
# matrix_1 = [[int(input("Enter num for matrix-1 >>> ")) for _ in range(n)]for _ in range(n)]
# matrix_2 = [[int(input("Enter num for matrix-2 >>> ")) for _ in range(n)]for _ in range(n)]
# matrix_3 = [['_'] * n for _ in range(n)]
# for row in range(n):
#     for col in range(n):
#         matrix_3[row][col] = matrix_1[row][col] if matrix_1[row][col] >= matrix_2[row][col] else matrix_2[row][col]
# for i in matrix_3:
#     print(i)

# 14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.

# n = 10
# matrix = [[b * a for b in range(1, n + 1)] for a in range(1, n + 1)]
# print('Before:')
# for row in range(n):
#     for col in range(n):
#         print(str(matrix[row][col]).ljust(2), end=' ')
#     print()
#
# for i in range(n):
#     matrix[i][i] = matrix[i][n - i - 1]
#     matrix[i][n - i - 1] = matrix[i][i]
#
# print('After:')
# for row in range(n):
#     for col in range(n):
#         print(str(matrix[row][col]).ljust(2), end=' ')
#     print()

# 15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.

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
