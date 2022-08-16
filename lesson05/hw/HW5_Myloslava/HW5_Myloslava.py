#task 1
import random
n = random.randint(0, 100)
print(n)

att = 0
while att <= 10:
    number = int(input())
    if n > number:
        att += 1
        print("The random number is bigger")
    elif n < number:
        att += 1
        print("The random is smaller")
    elif n == number:
        att = 10
        print("Winner")

# task 2
