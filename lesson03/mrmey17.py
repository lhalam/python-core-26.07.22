import random

def task_one():
    the_zen_of_python = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

    print('Word count "better":', the_zen_of_python.count('better'), '\n'
          'Word count "never":', the_zen_of_python.count('never'), '\n'
          'Word count "is":', the_zen_of_python.count('is'))

    print(the_zen_of_python.upper())
    the_zen_of_python = the_zen_of_python.replace('i', '&')

#--------------------------------------------------------------------------------

def task_two(num):
    print(f'Случайное число: {num}')
    multiple = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
    print(f'{num[0]}*{num[1]}*{num[2]}*{num[3]} =', multiple)
    print('Перевернутое умножение всех цифр =', str(multiple)[::-1])
    print('Перестановка цифр:', num[2]+num[0]+num[1]+num[3],
    num[3]+num[1]+num[2]+num[0],
    num[1]+num[3]+num[0]+num[2],
    num[0]+num[2]+num[3]+num[1], sep='\n')
#--------------------------------------------------------------------------------

def task_three(a, b):
    print(f'Первая переменная = {a}, вторая переменная = {b}')
    a, b = b, a
    print(f'Первая переменная теперь = {a} (второй), вторая переменная теперь {b} (первой)')



print('\tЗАДАЧА НОМЕР 1\n')
task_one()
print('\n\tЗАДАЧА НОМЕР 2\n')
task_two(str(random.randint(1000, 9999)))
print('\n\tЗАДАЧА НОМЕР 3\n')
task_three(input('Введите переменную 1: '), input('Введите переменную 2: '))