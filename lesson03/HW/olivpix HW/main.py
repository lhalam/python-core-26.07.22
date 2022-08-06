# 1. Записати в стрічку філософію Пайтон
zen = open("zen.py")
zentext = zen.read()
# print(zentext)

# Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('\nbetter -', zentext.count("better"))
print('never -', zentext.count("never"))
print('is -', zentext.count("is"))

# Вивести весь текст у верхньому регістрі (всі великі літери)
print("\n", zentext.upper())

# Замінити всі входження символу “і” на “&”
print(zentext.replace("i", "&"), "\n")

zen.close()
#________________________________________________________________________
# 2. Задано чотирицифрове натуральне число.
num = 8369
print(num)

# Знайти добуток цифр цього числа
numstr=str(num)
print(int(numstr[0]) * int(numstr[1]) * int(numstr[2]) * int(numstr[3]))

# Записати число в реверсному порядку.
print(numstr[::-1])

# Посортувати цифри, що входять в дане число
numlist = list(numstr)
numlist.sort()
print(numlist)

# 3.Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
s = 66
f = 2
s, f = f, s
print(s, f)