from random import randint
import pprint
"1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в"
"третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран."

# lj = [randint(-1000, 1000) for _ in range(10)]
# li = [int(input('Enter number: ')) for _ in range(10)]
# lk = []
# for i in range(len(li)):
#     lk.append(li[i] + lj[i])
# print(f'First list (random): {lj}\nSecond list (input): {li}\nSum elements = {lk}')


"2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку."
"Вивести на екран сам список, отримані суму і добуток його елементів."

# l, summa, mult = [], 0, 1
# for i in range(10):
#     s = int(input('Enter number - '))
#     l.append(s)
#     summa += s
#     mult *= s
# print(l, '\n' 'Summary el =', summa, '\n' 'Multiple el =', mult)


"3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список."
"Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості."

# l = [randint(-5, 4) for _ in range(20)]
# neg = len(list(filter(lambda x: x < 0, l)))
# pos = len(list(filter(lambda x: x > 0, l)))
# zero = len(list(filter(lambda x: x == 0, l)))
# print(f'{l}\nNegative numbers = {neg}\nPositive numbers = {pos}\nZeros = {zero}')

'4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні. ' \
'Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.'

# l_pos, l_neg = [], []
# for i in range(20):
#     rand_n = randint(-5, 5)
#     print(rand_n, end=', ')
#     if not rand_n:
#         continue
#     l_pos.append(rand_n) if rand_n > 0 else l_neg.append(rand_n)
# print(f'\nPositive list: {l_pos}\nNegative list: {l_neg}')

'5. Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.'

# l = [randint(-99, 99) for _ in range(20) if _ != 0]
# print(l)
# # l = list(filter(lambda x: x > 0, l))
# # print(l)
# neg = []
# for i in l:
#     if i < 0:
#         neg.append(i)
# for i in neg:
#     l.remove(i)
# print(l)

'6. У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, ' \
'то  другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого масиву стоять парні числа.'

# l = [randint(1, 99) for _ in range(10)]
# print(l)
# l_index = [l.index(i) for i in l if not i % 2]
# print(l_index)

'7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.'

# l = ['a', 'b', 'a', 'c', 'c', 'd', 'e', 1, 2, 3, 1, 2]
# l1 = [i for i in l if l.count(i) == 1]
# print(l1)

'8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.'

# l = [randint(1, 99) for _ in range(10)]
# max_el, min_el = max(l), min(l)
# l[l.index(max_el)], l[l.index(min_el)] = l[l.index(min_el)], l[l.index(max_el)] #???

'9. Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.'

# matrix = [[randint(1, 9) for _ in range(8)] for _ in range(8)]
# li = [[]]
#
# for i in range(len(matrix)):
#     summa_rows, summa_col = 0, 0
#     for j in range(len(matrix[i])):
#         summa_rows += matrix[i][j]
#         summa_col += matrix[j][i]
#     matrix[i].append(summa_rows)
#     li[0].append(summa_col)
# matrix += li
# pprint.pprint(matrix)

'10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.'

# matrix = [[randint(0, 999) for _ in range(8)] for _ in range(8)]
# pprint.pprint(matrix)
# l = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if len(str(matrix[i][j])) == 2:
#             l.append(matrix[i][j])
# print('Double digits numbers:', len(l), '-', l)

'11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). ' \
'Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.'

# matrix = [['_'] * 5 for _ in range(4)]
#
# for row in range(3):
#     for col in range(5):
#         matrix[row][col] = int(input('Enter num: '))
#
# for i in range(len(matrix[-1])):
#     matrix[-1][i] = matrix[0][i] + matrix[1][i] + matrix[2][i]
#
# for row in matrix:
#     print(*row)

'12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.'

# matrix = [[randint(-10, 10) for _ in range(5)] for _ in range(5)]
# l_min = [min(i) for i in matrix]
# print(max(l_min))

'13. Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох.'

# n = 5
# matrix_one = [['_'] * n for _ in range(n)]
# matrix_two = [['_'] * n for _ in range(n)]
# matrix_three = [['_'] * n for _ in range(n)]
#
# for row in range(len(matrix_one)):
#     for col in range(len(matrix_one[row])):
#         matrix_one[row][col] = int(input('Enter num for matrix-1: '))
# print()
# for row in range(len(matrix_two)):
#     for col in range(len(matrix_two[row])):
#         matrix_two[row][col] = int(input('Enter num for matrix-2: '))
#
# for row in range(len(matrix_three)):
#     for col in range(len(matrix_three[row])):
#         matrix_three[row][col] = matrix_one[row][col] if matrix_one[row][col] >= matrix_two[row][col] else matrix_two[row][col]
# pprint.pprint(matrix_three)

'14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.'

# n = 10
# matrix = [[b * a for b in range(1, n + 1)] for a in range(1, n + 1)]
# # pprint.pprint(matrix)
# print('Before:')
# for row in range(n):
#     for col in range(n):
#         print(str(matrix[row][col]).ljust(3), end=' ')
#     print()
#
# for i in range(n):
#     matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
#
# print('After:')
# for row in range(n):
#     for col in range(n):
#         print(str(matrix[row][col]).ljust(3), end=' ')
#     print()
# # pprint.pprint(matrix)

'15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.'

# matrix = [[randint(-10, 10) for _ in range(5)] for _ in range(5)]
matrix = [[3, 2, 1, 5, 4],
          [3, 4, 5, 7, 9],
          [4, 5, 6, 7, 8],
          [1, 3, 4, 5, 0],
          [2, 4, 6, 8, 9]]
matrix_2 = [['_' for _ in range(5)] for _ in range(5)]

pprint.pprint(matrix)

print()

matrix_copy = matrix[0].copy()
matrix_copy.sort()
list_index = []

for index in matrix_copy:
    list_index.append(matrix[0].index(index))

for x in range(5):
    index = 0
    for y in list_index:
        # print('xy', matrix[x][y])
        # print('pop=', matrix[x].pop(y))
        # pop = matrix[x].pop(y)
        # print('pop =', pop)
        # matrix[x].insert(0, pop)
        matrix_2[x][index] = matrix[x][y]
        index += 1

# print()
# pprint.pprint(matrix)
print()
pprint.pprint(matrix_2)


# # # for i in range(5):
# # #     for j in range(5):
# # #         # matrix[i][j], matrix[i][matrix_copy.index(matrix[i][j])] = matrix[i][matrix_copy.index(matrix[i][j])], matrix[i][j]
# #
# # # for x in range(5):
# # # for y in range(5):
# # #     matrix[0][y], matrix[0][matrix_copy.index(matrix[0][y])] = matrix[0][matrix_copy.index(matrix[0][y])], matrix[0][y]
# # index = matrix_copy.index
# # # matrix[0][0], matrix[0][matrix_copy.index(matrix[0][0])] = matrix[0][matrix_copy.index(matrix[0][0])], matrix[0][0]
# # # matrix[0][0], matrix[0][index(matrix[0][0])] = matrix[0][index(matrix[0][0])], matrix[0][0]
# # a = matrix[0][0]
# # # b = matrix[0][index(matrix[0][0])]
# # b = matrix[0][2]
# # print(f'a = {a}, b = {b}')
# # a, b = b, a
# # # a = b
# # # print('index =', index(matrix[0][0]))
# # # matrix[0][0], matrix[0][2] = matrix[0][2], matrix[0][0]
# # # print(matrix[0][0], matrix[0][matrix_copy.index(matrix[0][0])], matrix[0][matrix_copy.index(matrix[0][0])], matrix[0][0])
# # print(matrix[0][0], matrix[0][index(matrix[0][0])], matrix[0][index(matrix[0][0])], matrix[0][0])
# #
# # print(matrix_copy.index(matrix[0][0]))
# matrix[0][3], matrix[0][4] = matrix[0][4], matrix[0][3]
# matrix[0][0], matrix[0][2] = matrix[0][2], matrix[0][0]
# matrix[0][4] = matrix[0][0]
#
#
# # for i in range(5):
#
# for j in range(-1, -6, -1):
#
#     index = matrix[0].index(matrix_copy[j])
#     pop = matrix[0].pop(matrix[0].index(matrix_copy[j]))
#     list_index.append(index)
#     print(f'matrix[{0}]:', matrix[0])
#     print('pop=', pop, 'index =', index)
#     matrix[0].insert(0, pop)
# print(list_index)
# # print(matrix[0].index(matrix_copy[0]))
#
# print()
# pprint.pprint(matrix)
#
# # list.pop(), list.insert()
#
# # list1 = [3, 2, 1, 4, 5, 6]
# # list1.insert(0, list1.pop(2))
#
#
# # for i in range(-1, -6, -1):
# #     for j in range(-1, -6, -1):
# #         pop = matrix[0].pop(matrix[0].index(matrix_copy[i]))
# #         print('pop=', pop)
# #         matrix[0].insert(0, pop)
#Я решил не удалять мои страдания