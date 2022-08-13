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

ls, dod, vid, zer = [],[],[],[]
for i in range(20):
    numb = randrange(-5, 4)
    ls.append(numb)
    if numb > 0:
        dod.append(numb)
    elif numb < 0:
        vid.append(numb)
    else:
        zer.append(numb)
print(f"кількість додатніх = {len(dod)}, ось вони - {dod}")
print(f"кількість відємних = {len(vid)}, ось вони - {vid}")
print(f"кількість нульових = {len(zer)}, ось вони - {zer}")
