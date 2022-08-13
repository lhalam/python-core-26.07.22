#1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
# в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.
from random import randint
from random import randrange
#
# ls_one = list(range(randint(1,30)))
#
# n = int(input("please, input the length of second list - "))
# ls_two, ls_three = [],[]
# while n>0:
#     ls_two.append(int(input("please, input numer - ")))
#     n -=1
#
# for i in range(min(len(ls_one), len(ls_two))):
#     ls_three.append(ls_one[i] + ls_two[i])
# ls_three = ls_three + (ls_one[len(ls_three):] if len(ls_one)>len(ls_two) else ls_two[len(ls_three):])
#
# print("first list -  ", ls_one)
# print("second list - ", ls_two)
# print("third list -  ", ls_three)

#2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку.
# Вивести на екран сам список, отримані суму і добуток його елементів.

# n = int(input("please, input the length of second list - "))
# ls, dob = [],1
# while n>0:
#     numb = int(input("please, input numer - "))
#     ls.append(numb)
#     dob *= numb
#     n -= 1
# print(f"Summa = {sum(ls)}")
# print(f"Dobutok = {dob}")

#3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.

# ls, dod, vid = [],0, 0
# for _ in range(20):
#     numb = randrange(-5, 4)
#     ls.append(numb)
#     if numb > 0:
#         dod += 1
#     elif numb < 0:
#         vid += 1
#
# print("список - ", ls)
# print(f"кількість додатніх = {dod}")
# print(f"кількість відємних = {vid}")
# print(f"кількість нульових = {ls.count(0)}")

#4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
# Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

# ls = [randrange(-5, 5) for _ in range(int(input("input length of list - ")))]
# pl, mn = [], []
# for i in ls:
#     if i>0:
#         pl.append(i)
#     elif i<0:
#         mn.append(i)
#
# print("all numbers - ", ls)
# print("dodatni - ", pl)
# print("videmni - ", mn)

#5. Заповнити список випадковими додатними і від’ємними цілими числами.
# Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.

# ls = [randrange(-10,10) for _ in range(int(input("Input length of list - ")))]
# print("original list - ", ls)
# lst = ls.copy()
# for i in range(len(ls)):
#     if ls[i]<0:
#         lst.remove(ls[i])
# print("edited list - ", lst)

#6. У другому списку зберегти індекси парних елементів першого списку.
# Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
# то другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля),
# оскільки саме в цих позиціях першого масиву стоять парні числа.

# ls = [randrange(0, 30) for _ in range(int(input("input length of list - ")))]
# print("original list - ", ls)
# lst = []
# for i in range(len(ls)):
#     if ls[i] % 2 == 0:
#         lst.append(i)
# print("list of even indexes - ", lst)

#7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.

# ls = [randrange(0, 30) for _ in range(int(input("input length of list - ")))]
# print("original list - ", * sorted(ls))
# tpl = set(ls)
# print("not repeated numbers in list - ", * tpl)

#8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

ls = [randrange(0, 30) for _ in range(int(input("input length of list - ")))]
print("original list - ", * ls)
print(f"max number - {max(ls)}, index - {ls.index(max(ls))}")
print(f"min number - {min(ls)}, index - {ls.index(min(ls))}")
ls[ls.index(max(ls))], ls[ls.index(min(ls))] = min(ls), max(ls)
print("changed list - ", * ls)