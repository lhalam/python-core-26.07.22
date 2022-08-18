# 1. Заповнити один список випадковими числами,
# інший - введеними з клавіатури числами,
# в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.

import random
#
# first_list = random.sample(range(1, 999), 5)
# print(f"List with 5 random numbers: ", first_list)
# second_list = []
# for i in range(5):
#     second_list.append(int(input("Enter your numbers: ")))
# print(f"Inputed list: ", second_list)
#
# third_list = [first_list, second_list]
# print (f"List with 5 random numbers: ", first_list, f"Inputed list: ", second_list, f"Sum of each element:", [sum(x) for x in zip(*third_list )])

# "2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку."
# "Вивести на екран сам список, отримані суму і добуток його елементів."

# my_list = []
# for k in range(5):
#     my_list.append(int(input()))
# product = 1
# for item in my_list:
#     product = product * item
# print(f"List: ", my_list, f'sum of list:', sum(my_list), f'prod of list: ', product )

# 3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список."
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.
#
# randomlist = []
# for i in range(20):
#     n = random.randint(-5,4)
#     randomlist.append(n)
# print(randomlist)
# pos = (len([ele for ele in randomlist if ele > 0]) / len(randomlist)) * 100
# neg = (len([ele for ele in randomlist if ele < 0]) / len(randomlist)) * 100
# etc = (len([ele for ele in randomlist if ele == 0]) / len(randomlist)) * 100
# print(f'Pos elements was: ',pos, "%", 'negative: ', neg, '%','and zero: ', etc, '%')

# 4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
# Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

# x_list, pos_list, neg_list = [], [], []
# for u in range(20):
#     n = random.randint(-5,5)
#     x_list.append(n)
# print(x_list)
# pos_list = [n for n in x_list if n > 0]
# neg_list = [n for n in x_list if n < 0]
# print(f"Positive list: {pos_list}, and negative: {neg_list}")

# 5. Заповнити список випадковими додатними і від’ємними цілими числами.
# Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.

# r_list = []
# for l in range(10):
#     n = random.randint(-100, 100)
#     r_list.append(n)
# print(r_list)
# p = []
# for g in r_list:
#     if g < 0:
#         p.append(g)
# for g in p:
#     r_list.remove(g)
# print(r_list)

# 6. У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, ' \
# то  другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого масиву стоять парні числа.'

# r = []
# for h in range(10):
#     m = random.randint(-100, 100)
#     r.append(m)
# print(r)
# r_ind = []
# for i in r:
#     if i % 2 == 0:
#         r_ind.append(i)
# print(r_ind)

# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.
#
# list1 = []
# for i in range(10):
#     t = random.randint(1, 10)
#     list1.append(t)
# print(list1)
# list2 = [i for i in list1 if list1.count(i)==1]
# print(f'non repeated nums: {list2}')

# 8 У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

# another_list = [random.randint(1, 99) for _ in range(10)]
# print(another_list)
# min_val, max_val = min(another_list), max(another_list)
# print(min_val, max_val)
# imx, imin = another_list.index(max_val), another_list.index(min_val)
# another_list.remove(min_val), another_list.insert(imx, min_val), another_list.remove(max_val), another_list.insert(imin, max_val)
# print(another_list)

# '9. Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.'
import numpy as np

M = [[1,2,3],\
    [4,5,6],\
    [7,8,9]]
print(M)
col, arr = np.sum(M,axis=0), np.sum(M,axis=1)
print(f'sum of columns: {col}, sum of array: {arr}')








# 10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.

