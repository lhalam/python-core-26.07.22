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

# ls = [randrange(0, 30) for _ in range(int(input("input length of list - ")))]
# print("original list - ", * ls)
# print(f"max number - {max(ls)}, index - {ls.index(max(ls))}")
# print(f"min number - {min(ls)}, index - {ls.index(min(ls))}")
# ls[ls.index(max(ls))], ls[ls.index(min(ls))] = min(ls), max(ls)
# print("changed list - ", * ls)

#9. Порахувати суми кожного рядка і кожного стовпця матриці.
# Доповнити її стовпцем, який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

#10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.

# mx = []
# count = 0
# width, height = int(input("input width of matrix - ")),int(input("input height of matrix - "))
# for i in range(width):
#     mx.append([])
#     for j in range(height):
#         mx[i].append(randrange(0,999))
#         print(mx[i][j], end=" ")
#         count +=1 if 9<mx[i][j]<100 else 0
#     print(end="\n")
# print(f"double numbers = {count}")

#11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
# Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.

#12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

#13. Дві матриці заповнюються введенням з клавіатури.
# елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох.

mx_one, mx_two, mx_three = [], [], []
width, height = int(input("input width of matrix - ")), int(input("input height of matrix - "))
print("input your 1 - matrix:")
for i in range(width):
    mx_one.append([])
    for j in range(height):
        mx_one[i].append(int(input(f"{i, j} = ")))
print("input your 2 - matrix:")
for i in range(width):
    mx_two.append([])
    mx_three.append([])
    for j in range(height):
        mx_two[i].append(int(input(f"{i, j} = ")))
        mx_three[i].append(max(mx_one[i][j], mx_two[i][j]))

print("first matrix:", mx_one)
print("second matrix:", mx_two)
print("new best matrix:")
print(*mx_three)

#14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.

# mx = []
# width, height = 10, 10
# for i in range(width):
#     mx.append([])
#     for _ in range(height):
#         mx[i].append(randrange(0,999))
#     mx[i][0],mx[i][-1] = mx[i][-1], mx[i][0]
#     print(* mx[i])

#15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.

# mx = []
# width, height = int(input("input width of matrix - ")),int(input("input height of matrix - "))
# for i in range(width):
#     mx.append([])
#     for j in range(height):
#         mx[i].append(randrange(0,999))
#     if i == 0:
#         mx[i] = sorted(mx[i])
#     print(* mx[i])