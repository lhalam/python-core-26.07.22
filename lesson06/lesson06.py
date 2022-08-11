# # list
# # l = list()
# # print(l)
# # l = list("123456")
# # print(l)
# # l = list((1, 2, 3))
# # print(l)
# # # l = list(1)
# # # print(l)
# # l = []
# # print(l)
# # l = [1,2,3,4]
# # print(l)
# # l = ["123456"]
# # print(l)
# # l = list(range(10))
# # print(l)
#
# a = [1, 2, 3, 4]
# #
# # b = [1,2,3,4,2,a]
# # c = b
# # d = b.copy()
# # import copy
# # dd = copy.deepcopy(b)
# #
# # print("b:\t", b)
# # print("c:\t", c)
# # print("d:\t", d)
# # print("dd:\t", dd)
# # a[0]="AA"
# # print("b:\t", b)
# # print("c:\t", c)
# # print("d:\t", d)
# # print("dd:\t", dd)
# # print(b.count(2))
# print(a + a)
# # a.append(1)
# # a.append(a)
# # print(a)
# # print(a[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][1])
# a.extend("sgdvcfhsgvjhsfd")
# print(a)
# print(a.index("v"))
# # print(a.index("x"))
# a.insert(1, "stest")
# a.insert(10000, "end")
# a.insert(-10000, "start")
# # print(a)
# # aa = a.pop()
# # print(aa , a)
# # aa = a.pop(1)
# # print(aa , a)
# a.append(1)
# aa = a.remove(1)
# aa = a.remove("stest")
# print(aa, a)
#
# aa = a.reverse()
# print(aa, a)
#
#
# def f(a):
#     s = 0
#     if isinstance(a, int):
#         s = a
#     elif isinstance(a, str):
#
#         for i in a:
#             s += ord(i)
#     return s
#
#
# # a.sort(key=lambda a: ord(a) if isinstance(a, str) else a)
# # a.sort(key=f)
# # print(a)
# #
# # c = [1, 2, 6, 3, 4, 6, 7]
# # c.sort()
# # print(c)
# # print([1,2,3]*3)
# # print([[]*3]*3)
# # print([i for i in dir(list) if not i.startswith("_")])
# #
# # for i in enumerate(list("abcd")):
# #     print(i)
# # for i, v in enumerate(list("abcd")):
# #     print(i, v)
# # a = list(enumerate(list("abcd")))
# # print(a)
# # print(type(a[0]))
# #
# # a = [1,3,6,2,3,6,8,9,3,5,76]
# # a = sorted(a)
# # print(a)
# # print(b)
# #
# # a = [1,3,6,2,3,6,8,9,3,5,76]
# # a = a.sort()
# # print(a)
# # print(b)
#
#
# r = range(1000)
#
# print(r)
# print(r.start)
# print(r.step)
# print(r.index(17))
# print(r.__sizeof__())
# print(list(r).__sizeof__())
#
# l = []
# for i in range(4):
#     for j in range(i):
#         l.append((i, j))
#
# print(l)
# l = [(i, j) for i in range(4) for j in range(i)]
# print(l)

# ## tuple
# t = tuple()
# print(t)
# t = tuple("sdvfj")
# print(t)
# t = ()
# print(t)
# t = (1, )
# print(t)
# # t = (1)
# # print(t)
# # t[0] = 1
#
# l = list(range(1000))
# t = tuple(range(1000))
# print(l.__sizeof__())
# print(t.__sizeof__())
# t = (i for i in range(10))
#
# print(t)
# print(next(t))
# print(next(t))
# print(next(t))
# t = [i for i in range(10)]
#
# print(t)

# set
# s = set()
# print(s)
# s = set("vfbgxudfvgbdsjhgvdsjhgvfdsaugvfhsdgvdh")
# print(s)
# s = {1, 2, 3, 1, 2, 31, 32, 4}
# print(s)
# print(1 in s)
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.union(s2))
# print(s1.issubset(s2))
# print(s1.intersection(s2))

## dict

d = dict()
print(d)
d = {}
print(d)
d = {"a": 1, "b": 2, "c": {'a': [1, 21, 3, 4], 1: 25}}
print(d)
# d = {(1, 2, 3): 1}
# print(d)
print([i for i in dir(dict) if not i.startswith("_")])
# s = set([1,2,5,3,5,7,3,2,5,78,9,4,23,2,4,6])
# s = sorted(list(s))
# print(s)
for key in d:
    print(key, d[key])
for item in d.items():
    print(item)
for key, value in d.items():
    print(key, value)
d["new"] = 25
d["b"] = 25
print(d)
print(d["b"])
print(d.get("b"))
print(d.get("bb"))
print(d.keys())
print(d.values())