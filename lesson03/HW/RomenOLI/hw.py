zen = """Beautiful is better than ugly.
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

#Знайти в заданій стрічці кількість входжень слів (better, never, is)
count_sub_str = zen.count("better") + zen.count("never") + zen.count("is")
print(f"кількість входжень - {count_sub_str}")

#Вивести весь текст у верхньому регістрі (всі великі літери)
print(zen.upper())

#Замінити всі входження символу “і” на “&”
print(zen.replace("i", "&"))

#Задано чотирицифрове натуральне число.
n = input("введи чотирицифрове натуральне число тут - ")
#Знайти добуток цифр цього числа.
print(f"добуток = {int(n[0]) * int(n[1]) * int(n[2]) * int(n[3])}")

#Записати число в реверсному порядку.
print(f"число в реверсному порядку - {n[::-1]}")

#Посортувати цифри, що входять в дане число
print(f"відсортоване число - {''.join(sorted(n))}")

#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a, b = input("введи значення першої змінної - "), input("введи значення другої змінної - ")
print(f"перед обміном. перша змінна-{a}, друга змінна -{b}")
a, b = b, a
print(f"після обміну. перша змінна-{a}, друга змінна -{b}")