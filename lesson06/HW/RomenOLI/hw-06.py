#1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
# в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.
from random import randint

ls_one = list(range(randint(1,30)))

n = int(input("please, input the length of second list - "))
ls_two, ls_three = [],[]
while n>0:
    ls_two.append(int(input("please, input numer - ")))
    n -=1

for i in range(min(len(ls_one), len(ls_two))):
    ls_three.append(ls_one[i] + ls_two[i])
ls_three = ls_three + (ls_one[len(ls_three):] if len(ls_one)>len(ls_two) else ls_two[len(ls_three):])

print("first list -  ", ls_one)
print("second list - ", ls_two)
print("third list -  ", ls_three)