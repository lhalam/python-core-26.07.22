# def print_hello():
#     """
#     print string Test
#     :return: None
#     """
#     print("hello")
#
# print_hello()
#
# a = print_hello()
# print(a)
#
# help(print_hello)

# def my_sum(a, b):
#     c = a + b
#     print(f"a+b={c}")
#     print("a+b=", c, sep="")
#     print("a+b="+str(c))
#     print("a+b={}".format(c))
#     return c
#
#
# print(my_sum(12, 5))
# print(my_sum(32, 5))
# print(my_sum(52, 5))
# print(my_sum(42, 5))

# def f(a, b):
#     return f"{a=} {b=}"
# # f()
# # f(1)
# print(f(1,2))
# print(f(b=1, a=2))
# def print_date(day, month, year, sep):
#     print(f"{day}{sep}{month}{sep}{year}")
#
# print_date(18, 8, 2022, "/")
# print_date(18, 8, 2022, ":")
# print_date(8, 18, 2022, "/")
# print_date(month=8, day=18, year=2022, sep="/")
# print_date(year=2022, sep="/", month=8, day=18)
# def print_date(day, month, year, sep):
#     return f"{day}{sep}{month}{sep}{year}"
#
#
# a = print_date(year=2022, sep="/", month=8, day=18)
# print(a)
#
#
# def print_date(day, month, year=2022, sep="/"):
#     return f"{day}{sep}{month}{sep}{year}"
#
#
# print(print_date(18, 8))
# print(print_date(18, 8, 4000))
# print(print_date(18, 8, 4000, sep="*"))
#
# def print_date(day, month=200, year=2022, sep="/"):
#     return f"{day}{sep}{month}{sep}{year}"
#
# print(print_date(20))
# #print(print_date(20,20,20,20,20))
# def f(a, b, *args, c=3, d=4, **kwargs):
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs=}")
#
#
# f(1, 2)
# f(1, 2, 3)
# f(1, 2, 3, 4, 5, 6, 7, 8, 9)
# f(1, 2, 3, 4, 5, 6, 7, 8, 9, c=901, f=555, r="jhvvdsbj", sep="hfdvb")
#
# l = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# f(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
# f(*l)
# print(*l)
# d = {
#     "a": 11,
#     "b": 22,
#     "c": 33,
# }
# f(*d)
# f(**d)
# f(a=d["a"], b=d["b"], c=d["c"])

# def f(l=[]):
#     l.append(1)
#     print(l)
#
#
# f()
# f()
# f()
# f([2, 3])
# f()
# f([11, 322])
# f()
# print(l)
# MAX = 100
# print(1, dir())
# def f():
#     global MAX
#     MAX = 200
#     print(3, dir())
#     print(MAX)
# print(2, dir())
# f()
# print(MAX)
# c =10
#
def f(n):
    c = 0

    def d(text):
        nonlocal c
        c += 1
        print(c, text, n)

    return d


# g = f(5)
# g("a")
# g("b")
# g("c")
# g("d")
# g = f(5)
# g("d")

ff = lambda a, b, c: f([a,b,c])
g = ff(1, 2, 3)
g("abc")
