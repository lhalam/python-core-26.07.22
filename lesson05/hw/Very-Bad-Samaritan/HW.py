import random

print("Task 1")

jackpot = random.randint(0, 100)

for i in range(10):
    guess = int(input("Make your bet!\n"))
    if guess == jackpot:
        print("You won! Well, house not always wins")
        break
    elif guess > jackpot:
        print("Well, that was too high, wasn't it?")
    elif guess < jackpot:
        print("Rise your stakes, ladies and gentlemen!")
else:
    print("Well, that was unlucky. The house always wins! The jackpot number was", jackpot)


print("Task 2")

print("Please, enter 10 numbers greater than 2")
counter = 0
for i in range(10):
    a = int(input())
    if a % 5 == 0:
        counter += 1
print("Amount of multiples of 5 =", counter)


print("Task 3")

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
    print("\n")


print("Task 4")

for i in range(20):
    for j in range(40):
        if i == 0 or i == 19 or j == 0 or j == 39:
            print("X", end="")
        else:
            print("O", end="")
    print("\n", end="")


print("Task 5")

p = 15
h = 47
a = 0
sum_numb = 0
mult = 1
counter = 0
while not (a == p or a == h):
    a = int(input("Please, enter a number:"))
    if a < p:
        sum_numb += a
    if a > h:
        mult *= a
    if p < a < h:
        counter += 1

print("\nSum =", sum_numb, "\nMult =", mult, "\nCounter =", counter)


print("Task 6")

a = None
counter_1 = 0
counter_2 = 0
while not a == 0:
    a = int(input("Please, enter a number:"))
    if a > 0:
        counter_1 += 1
    elif a < 0:
        counter_2 += 1

perc_1 = counter_1 / (counter_1 + counter_2) * 100
perc_2 = counter_2 / (counter_1 + counter_2) * 100
print("Percent of positive numbers is:", perc_1, "%")
print("Percent of negative numbers is:", perc_2, "%")