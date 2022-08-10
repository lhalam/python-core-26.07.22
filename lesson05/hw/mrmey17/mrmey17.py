"1. У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен його відгадати не більше ніж за 10 спроб."
"Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане."
"Якщо за 10 спроб число не відгадане, то вивести загадане число."

from random import randint

def guess_the_number():
    rand_num = randint(0, 100)
    #print(rand_num)
    try_count = 10
    for _ in range(10):
        try_to_guess = int(input('Try to guess the number: '))
        if try_to_guess == rand_num:
            print(f'You guessed the number!, "{rand_num}" was a hidden number')
            break
        elif try_to_guess < rand_num:
            print('The hidden number is greater than what you wrote')
        elif try_to_guess > rand_num:
            print('The hidden number is less than what you wrote')
        try_count -= 1
        print(f'Tries left {try_count}')
        while not try_count:
            print('Nice try but the given number was', rand_num)
            break

# guess_the_number()

"2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)"

# count_num = 0
# for _ in range(10):
#     if not int(input('Enter number: ')) % 5:
#         count_num += 1
# print(f'Numbers that are multiples of 5: {count_num}')

'3. Вивести на екран таблицю множення (від 1 до 9).'

def multiplication_table(num):
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print(f'{row} * {col} = {row * col}', end='\t\t')
        print()
# multiplication_table(9)

