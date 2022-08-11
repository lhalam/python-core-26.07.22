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
            print('Nice try, but the hidden number was', rand_num)
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

'4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів. ' \
'Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.'

# n, m = int(input('Enter number of rows: ')), int(input('Enter number of columns: '))
# symb_a, symb_b = input('Choose symbol 1 (perimeter): '), input('Choose symbol 2 (fill): ')
# for row in range(1, n + 1):
#     if row == 1 or row == n:
#         print(symb_a * m, end='\n')
#     else:
#         if m > 1:
#             print(symb_a + symb_b * (m-2) + symb_a, end='\n')
#         else:
#             print(symb_a * m, end='\n')

'''5. Дано число P і число H. Користувач вводить послідовність чисел. 
Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H; кількість чисел, що знаходяться в діапазоні
значень від P до H. При введенні числа рівного P або H, припинити обчислення та вивести результат. 
(не використовувати білдін функції)'''

# p, h = 5, 50
# flag = True
# sum_less_p, mult_greater_h, nums_in_range_ph = 0, 1, 0
#
# while flag:
#     n = int(input('Enter number: '))
#     if n < p:
#         sum_less_p += n
#     elif n > h:
#         mult_greater_h *= n
#     elif n in range(p + 1, h):
#         nums_in_range_ph += 1
#
#     if n == p or n == h:
#         if mult_greater_h != 1: print(f'Multiplication numbers greater than "{h}": {mult_greater_h}')
#         if sum_less_p != 0: print(f'Sum numbers less than "{p}": ', sum_less_p)
#         print('Num(s) in range between "P" and "H": ', nums_in_range_ph)
#         flag = False

