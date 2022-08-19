print("Task 1")

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

print("Uppercase text:\n", x.upper())

print("Better:", x.count("better"))
print("Never:", x.count("never"))
print("Is:", x.count("is"))

print("'I' is replaced with '$':", x.replace("i", "$"))


print("Task 2")

number = 1540
print("Number =", number)

num_str = str(number)
print("Product of numbers =", int(num_str[0]) * int(num_str[1]) * int(num_str[2]) * int(num_str[3]))

print("Number in reversed order =", num_str[::-1])

num_list = list(num_str)
num_list.sort()
print(num_list)


print("Task 3")

a_1 = 256
a_2 = 25565
print("a_1 =", a_1, "a_2 =", a_2)

a_1, a_2 = a_2, a_1
print("a_1 =", a_1, "a_2 =", a_2)
