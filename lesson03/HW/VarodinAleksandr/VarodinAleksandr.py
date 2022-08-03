# Task 1

text = '''Beautiful is better than ugly.
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
better = text.find('better')
print('better =', better)
count_is = text.find('is')
print('is =', count_is)
count_never = text.find('never')
print('never =' ,count_never)
upper_text = text.upper()
print(upper_text)
replaced_text = text.replace('i', '&')
print(replaced_text)

# Task 2

f = 8234
d = (f % 1000) % 10
c = (f % 100) // 10
b = (f // 100) % 10
a = f // 1000
t = a * b * c * d
print(t)
print(str(t)[::-1])
print(str(t).split())
string_t = str(t)
list_t = [string_t[0], string_t[1], string_t[2]]
list_t.sort()
k = ''.join(list_t)
print(k)

# Task 3

a = 5
b = 6
a, b = b, a
print(a, b)
