from random import randint

#task1
rand_num = randint(0, 100)
print(rand_num)
i = 0
while i <= 10:
    if i == 10:
        print(f"bida try off num is {rand_num}")
        break
    print(f"Try num = {i + 1}")
    user_ch = int(input("Input num "))
    if user_ch != rand_num:
        print("You num>rand_num" if user_ch > rand_num else "You num<rand_num")
        i += 1
        continue
    if user_ch == rand_num:
        print(f"You win num is = {user_ch}")
        break
    i += 1

#task2
j = 0
kol = 0
while j < 10:
    b = int(input("Input num >2"))
    if b > 2 and b % 5 == 0:
        kol += 1
        j += 1
        continue
    elif b <= 2:
        print("Incorrect num")
        j += 1
        continue
    else:
        j += 1
print(f"Kol num%5and>2 = {kol}")

#task3
for i in range(1, 9 + 1):
    print(*range(i, i * 9 + 1, i), sep='\t')

#task4
n = int(input("Input N"))
m = int(input("Input M"))
for i in range(n):
    print()
    for j in range(m):
        if i == 0 or j == 0 or j == m - 1 or i == n-1:
            print("*", end='')
        else:
            print("#", end='')

#task5
p = 10
h = 20
dob = 1
s = 0
kol = 0
while True:
    num = int(input("num = "))
    if num == p or num == h:
        print(f"dob = {dob} sum = {s} kol = {kol}")
        break
    elif num < p:
        s += num
    elif num > h:
        dob *= num
    if h > p and h > num > p:
        kol += 1
    elif h < p and h < num < p:
        kol += 1

#task6
kol_min = 0
kol_max = 0
i = 0
while True:
    num = int(input("num = "))
    if num == 0:
        break
    i += 1
    if num > 0:
        kol_max += 1
    else:
        kol_min += 1
    print(f"Percent pos = {kol_max*100/i}")
    print(f"Percent negative = {kol_min * 100 / i}")


