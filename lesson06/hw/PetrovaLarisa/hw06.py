print("""1 Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.""")
import random
l = []
r = []
s = []
for i in range(10):
    l.append(random.randint(0,100))
    r.append(int(input("Enter number: ")))
    s.append(l[i]+r[i])
print("Random numbers - ", l, "\nYou have entered - ",  r, "\nTheir sum - ", s)

print("""2 Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку.
Вивести на екран сам список, отримані суму і добуток його елементів.""")
l=[]
s = 0
d = 1
for i in range(10):
    l.append(float(input("Enter float number: ")))
    s += l[i]
    d *= l[i]
print("You have entered: ", l, "\nSum of elements - ", s, "\nProduct of elements - ", d)

print("""3 Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.""")

l = []
q_p = 0
q_n = 0
q_z = 0
for i in range(20):
    l.append(random.randint(-5, 4))
    if l[i] < 0:
        q_n += 1
    elif l[i] > 0:
        q_p += 1
    else:
       q_z += 1
print("List: ", l, "\nAmount of negative numbers: ", q_n, "\nAmount of positive numbers: ", q_p, "\nAmount of zeros: ", q_z)

print("""4 Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні,
 у другий - тільки від’ємні. Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.""")
l = []
lp = []
ln = []
for i in range(10):
    l.append(random.randint(-5, 5))
    if l[i] < 0:
        ln.append(l[i])
    elif l[i] > 0:
        lp.append(l[i])
print("List: ", l, "\nList of negative numbers: ", ln, '\nList of positive numbers: ', lp)

print("""5 Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран.
Видалити з списку всі від’ємні елементи і знову вивести.""")

l = []
for i in range(10):
    l.append(int(random.randint(-50, 50)))
print("List: ", l)
l = [i for i in l if i > 0]
print("Edited list: ", l)

print("""6 У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі
значеннями 8, 3, 15, 6, 4, 2, то другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля),
 оскільки саме в цих позиціях першого масиву стоять парні числа.""")

l1 = []
l2 = []
for i in range(10):
    l1.append(random.randint(0, 100))
    if l1[i]%2 == 0:
        l2.append(i)
print("List - ", l1, "List of indexes of even numbers - ", l2)

print("""7 У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.""")
l1 = [2, 20, 64, 547, 21, 5, 50, 64, 87, 2, 20]
print(l1)
for i in l1:
    if l1.count(i) == 1:
        print(i, end= " ")
print()
print("""8 У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.""")
for i in range(10):
    l.append(random.randint(1, 100))
print(l)
m1 = min(l)
m2 = max(l)
im1 = l.index(m1)
im2 = l.index(m2)
print("Min = ", m1, "max = ", m2, "position of min - ", im1, "position of max -", im2)
l.remove(m1)
l.insert(im2, m1)
l.remove(m2)
l.insert(im1, m2)
print(l)
print("""9 Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить суми елементів рядків
 та рядком, елементами якого є суми елементів стовпців.""")

N = [[2, 3, 4], [5, 1, 4], [6, 9, 7]]
print("N: ")
for i in range(3):
    for j in range(3):
        print(N[i][j], end = " ")
    print()
for i in range(3):
    N[i].append(sum(N[i]))
sum = 0
S = []
for i in range(4):
    for j in range(3):
      sum += N[j][i]
    S.append(sum)
    sum = 0
N.append(S)
print("N: ")
for i in range(4):
    for j in range(4):
        print("{:4}".format(N[i][j]), end = "")
    print()

print('''10 Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.''')
M = []
S = []
q = 0
for i in range(10):
    M = []
    for j in range(10):
        a = random.randint(0, 999)
        M.append(a)
        if (a > 9 and a < 100): q += 1
    S.append(M)
for i in range(10):
    for j in range(10):
        print("{:4}".format(S[i][j]), end = " ")
    print()
print("Amount of two-digit numbers: ", q)
print("""11 Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
 Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
 Наприкінці слід вивести отриману матрицю.""")
M = []
R = []
S = []
s = 0
for i in range(4):
    for j in range(4):
      t = int(input('Enter the number:  '))
      R.append(t)
      s += t
    M.append(R)
    R = []
    S.append(s)
    s = 0
M.append(S)
for i in range(5):
    for j in range(4):
        print("{:2}".format(M[i][j]), end = " ")
    print()

print("""12 Знайти максимальний елемент серед мінімальних елементів стовпців матриці.""")

list_min = []
for i in range(4):
    min = M[i][0]
    for j in range(4):
        if min > M[j][i]:
            min = M[j][i]
    list_min.append(min)
print("List of min elements of columns", list_min)
max_min = max(list_min)
print("Max of them: ", max_min)

print("""13 Дві матриці заповнюються введенням з клавіатури.
В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох.""")
ARow = []
BRow = []
CRow = []
A = []
B = []
C = []
for i in range(3):
    ARow = []
    BRow = []
    CRow = []
    for j in range(3):
        a = int(input("Enter the number for matrix A: "))
        b = int(input("Enter the number for matrix B: "))
        ARow.append(a)
        BRow.append(b)
        c = max(a, b)
        CRow.append(c)
    a = 0
    b = 0
    c = 0
    A.append(ARow)
    B.append(BRow)
    C.append(CRow)
print("A: ")
for i in range(3):
    for j in range(3):
        print("{:3}".format(A[i][j]), end = " ")
    print()
print("B: ")
for i in range(3):
    for j in range(3):
        print("{:3}".format(B[i][j]), end=" ")
    print()
print("C: ")
for i in range(3):
    for j in range(3):
        print("{:3}".format(C[i][j]), end=" ")
    print()

print("""14 У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.""")
S = []
for i in range(10):
    M = []
    for j in range(10):
        a = random.randint(0, 999)
        M.append(a)
        if (a > 9 and a < 100): q += 1
    S.append(M)
for i in range(10):
    for j in range(10):
        print("{:4}".format(S[i][j]), end = " ")
    print()
print()
for i in range(10):
    for j in range(10):
        if i == j:
           S[i][j], S[i][9-j] = S[i][9-j], S[i][j]
for i in range(10):
    for j in range(10):
        print("{:4}".format(S[i][j]), end = " ")
    print()

print("""15 Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.""")
min = S[0][0]
A = []
for i in range(10):
    n_min = i
    min = S[0][i]
    for j in range(i+1, 10):
        if S[0][j] < min:
            min = S[0][j]
            n_min = j
    for k in range(10):
        S[k][n_min], S[k][i] = S[k][i], S[k][n_min]
print("Sorted: ")
for i in range(10):
    for j in range(10):
        print("{:4}".format(S[i][j]), end = " ")
    print()

