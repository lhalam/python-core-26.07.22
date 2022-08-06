
x = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!
"""

print(x.upper())

print(x.count( "better" ))
print(x.count( "never" ))
print(x.count( "is" ))

print(x.replace( "i", "$"))

y = 4189
z = 4 * 1 * 8 * 9
print(z)

y = str(y)
print(y[::-1])

y = list(y)
y.sort()
print(y)

x = 5
y = 10
x, y = y, x
print(x)
print(y)