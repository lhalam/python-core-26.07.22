# 1. У програмі генерується випадкове ціле число від 0 до 100.
# Користувач повинен його відгадати не більше ніж за 10 спроб.
# Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# Якщо за 10 спроб число не відгадане, то вивести загадане число.число

from random import randint

random_number = randint(1, 100)
number_of_attemps = 10
while number_of_attemps != 0:
    guess_number = int(input("Enter number from 1 to 100: "))
    if random_number == guess_number:
        print(f"You win, number was{guess_number}")
        break
    else:
        number_of_attemps -= 1
        print("Your number is bigger" if guess_number > random_number else "Your number is smaller")
print(f"Random number was {random_number}")


