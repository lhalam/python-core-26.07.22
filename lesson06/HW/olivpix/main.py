import math
import random

# 1.Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в третій записати суми
# відповідних елементів перших двох. Вивести вміст списків на екран.

a = []
b = []
c = []
for i in range(7):
    n = random.randint(1, 100)
    a.append(n)
    l = int(input(f"b:{i+1} - "))
    b.append(l)
    c.append(n+l)
print("a:\t", a)
print("b:\t", b)
print("c:\t", c)

# 2.Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку.
# Вивести на екран сам список, отримані суму і добуток його елементів.

a = [int(input(f"a:{i+1} - ")) for i in range(7)]
print(a)
print(sum(a))
print(math.prod(a))

# 3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.

r = []
positive = 0
negative = 0
zero = 0
for i in range(20):
    n = random.randint(-5, 4)
    r.append(n)
    if n>0:
        positive += 1
    elif n<0:
        negative += 1
    else:
        zero += 1
print(r)
print(positive)
print(negative)
print(zero)

# 4.Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
# Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
pos = []
neg = []
ran = []
for i in range(10):
    n = random.randint(-5, 5)
    ran.append(n)
    if n>0:
        pos.append(n)
    elif n<0:
        neg.append(n)
print(f"Generated list: {ran}\n pos = {pos}\n neg = {neg}")

# 5.Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран.
# Видалити з списку всі від’ємні елементи і знову вивести.
g = [random.randint(-10, 10) for i in range(10)]
print("g:\t", g)
l = len(g)
i = 0
while i < l:
    if g[i] < 0:
        g.pop(i)
        l -= 1
    else:
        i += 1
print("g after deleting all neg num: \t:", g)

# 6. У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
# то другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого
# масиву стоять парні числа`.
g = [random.randint(1, 20) for i in range(10)]
f = [j for j in range(len(g)) if g[j]%2==0]
print(g)
print(f)

# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.
g = [random.randint(1, 15) for i in range(20)]
print("g: ", g)
j = [g[i] for i in range(len(g)) if g.count(g[i])==1]
print("Numbers that doesnt repeat: ", *j)

# 8.У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
g = [random.randint(1, 50) for i in range(20)]
print("g: ", g)
max_index=g.index(max(g))
min_index=g.index(min(g))
print(f"max = {max(g)} index_max = {max_index}")
print(f"min = {min(g)} index_min = {min_index}")
g[max_index], g[min_index] = g[min_index], g[max_index]
print("g: ", g)

# 9. Порахувати суми кожного рядка і кожного стовпця матриці.
# Доповнити її стовпцем, який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

le = int(input("Enter length: "))
he = int(input("Enter height: "))
m_list = [[random.randint(1, 5) for i in range(le)] for j in range(he)]
for i in m_list:
    print(*i)
col_list = []
c = 0
r = 0
for i in range(he):
    for j in range(le):
        r += m_list[i][j]
    m_list[i].append(r)
    r = 0
for i in range(le):
    for j in range(he):
        c += m_list[j][i]
    col_list.append(c)
    c = 0
m_list.append(col_list)
print("Final matrix:")
for i in m_list:
    print(*i)

# 10.Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.
le = int(input("Enter length: "))
he = int(input("Enter height: "))
matrix = [[random.randint(0, 999) for i in range(le)] for j in range(he)]
for i in matrix:
    print(i)
r = 0
for i in range(he):
    for j in range(le):
        if 9 < matrix[i][j] < 100:
            r += 1
print("Numbers that has two digits: ", r)

# 11.Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
# Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.
le = 5
he = 4
matrix = []
for i in range(he):
    mm = []
    matrix.append(mm)
    for j in range(le):
        matrix[i].append(int(input(f"Enter your number {j+1}: ")))
matrix.append(list(sum(matrix[i]) for i in range(he)))
for i in matrix:
     print(i)

# 12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці
le = int(input("Enter length: "))
he = int(input("Enter height: "))
matrix = [[random.randint(0, 100) for i in range(le)] for j in range(he)]
for i in matrix:
     print(i)
min_el = []
col_el = []
for i in range(le):
    col_el=[]
    for j in range(he):
        col_el.append(matrix[j][i])
    min_el.append(min(col_el))
print("Max from min: ", max(min_el))

# 13. Дві матриці заповнюються введенням з клавіатури.
# В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох.
le = int(input("Enter length: "))
he = int(input("Enter height: "))
f_matrix, s_matrix, t_matrix = [], [], []
for i in range(he):
    fmr = []
    smr = []
    tmr = []
    f_matrix.append(fmr)
    s_matrix.append(smr)
    t_matrix.append(tmr)
    for j in range(le):
        f_matrix[i].append(int(input(f"Enter ({i},{j}) in first matrix: ")))
        s_matrix[i].append(int(input(f"Enter ({i},{j}) in second matrix: ")))
        t_matrix[i].append(f_matrix[i][j] if f_matrix[i][j]>=s_matrix[i][j] else s_matrix[i][j])
print("First matrix: ")
for i in f_matrix:
    print(i)
print("Second matrix: ")
for i in s_matrix:
     print(i)
print("Third matrix: ")
for i in t_matrix:
     print(i)
# 14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.
lehe = 10
matrix = [[random.randint(-10, 20) for i in range(lehe)] for j in range(lehe)]
for j in matrix:
     print(j)
for i in range(lehe):
    x = -1-i
    matrix[i][i], matrix[i][x] = matrix[i][x], matrix[i][i]
print("\nFinal matrix:")
for j in matrix:
     print(j)


# 15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.
lehe = int(input("Enter size: "))
matrix = [[random.randint(-10, 20) for i in range(lehe)] for j in range(lehe)]
for j in matrix:
     print("\t", j)

for i in range(lehe):
    for j in range(lehe-1):
        if matrix[0][j]>matrix[0][j+1]:
            matrix[0][j], matrix[0][j + 1] = matrix[0][j + 1], matrix[0][j]
            for x in range(lehe-1):
                matrix[x+1][j], matrix[x+1][j + 1] = matrix[x+1][j + 1], matrix[x+1][j]
print("Final matrix:")
for j in matrix:
     print("\t", j)
