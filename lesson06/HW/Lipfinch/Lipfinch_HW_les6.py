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

# "3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список."
# "Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості."
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

# '4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні. ' \
# 'Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.'

x_list, pos_list, neg_list = [], [], []
for u in range(20):
    n = random.randint(-5,5)
    x_list.append(n)
print(x_list)
pos_list = [n for n in x_list if n > 0]
neg_list = [n for n in x_list if n < 0]
print(f"Positive list: {pos_list}, and negative: {neg_list}")