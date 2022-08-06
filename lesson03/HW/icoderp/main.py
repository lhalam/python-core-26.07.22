# 1 Записати в стрічку філософію Пайтона
filosofia_py = """The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!"""

# Знайти в заданій стрічці кількість входжень слів (better, never, is)
print(f"better: {filosofia_py.count('better')}")
print(f"never: {filosofia_py.count('never')}")
print(f"is: {filosofia_py.count('is')}\n")

# Вивести весь текст у верхньому регістрі (всі великі літери)
print(filosofia_py.upper())

# Замінити всі входження символу “і” на “&”
new_filosofia_py = filosofia_py.replace('i', '&')
print(new_filosofia_py, '\n')

# Задано чотирицифрове натуральне число.
num = 2143

# Знайти добуток цифр цього числа.
mult = int(str(num)[0]) * int(str(num)[1]) * int(str(num)[2]) * int(str(num)[3])
print(mult)

# Записати число в реверсному порядку.
num_str = str(num)
revers_num = num_str[::-1]
print(revers_num)

# Посортувати цифри, що входять в дане число
num_str = str(num)
# sort_num = sorted(num_str)
# print(*sort_num)
sort_num = list(num_str)
sort_num.sort()
print(*sort_num)

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = "Hello"
b = "Python"
a, b = b, a
print(a, b)
