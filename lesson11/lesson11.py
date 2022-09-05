# vec1 = [3, 10, 2, 1]
# vec2 = [-20, 5, 1]
# dot_mul = [u * v for u, v in zip(vec1, vec2)]
# l = []
# for i in range(min(len(vec1), len(vec2))):
#     l.append((vec1[i], vec2[i]))
# print(l)
# l = [(vec1[i], vec2[i]) for i in range(min(len(vec1), len(vec2)))]
# print(l)
# print(dot_mul)
# for i in zip(vec1, vec2):
#     print(i)
# print(zip(vec1, vec2))
# from functools import reduce
#
# l = ["4", "-1", 5, "-5", "4", "-1", 5, "-5", "4", "-1", 5, "-5"]
# l = map(int, l)
# l = [int(i) for i in l]
# print(l)
# l = filter(lambda x: x >= 0, l)
# # print(*l)
#
#
# def r(a, b):
#     print(a, b)
#     return a + b if b % 2 == 0 else a
#
# l  = [i for i in l]
# print(l)
# result = reduce(r, l, 0)
# print(result)


# name_str = "Liubov"
# custom_iterator = iter(name_str)
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
#
# class MyList:
#     def __init__(self):
#         self.i = -1
#         self.values = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#
#         if self.i > len(self.values) - 1:
#             raise StopIteration
#         return self.values[self.i]
#
#     def add(self, value):
#         self.values.append(value)
#
#
# a = MyList()
# a.add(1)
# a.add(2)
# a.add(3)
# a.add(4)
# a.add(5)
# for i in a:
#     print(i)
# else:
#     print("good")
# g = (i for i in range(500))
# i = [i for i in range(500)]
# print(g, g.__sizeof__())
# print(i, i.__sizeof__())
# print(*g)
# print(*g)
#
#
# def my_gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# g = my_gen()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def my_gen(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
#
# g = my_gen(4)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def my_decorator(func):
#     def inner(a, b):
#         print("I am going to sum", a, "and", b)
#         return func(a, b)
#
#     return inner
#
#
# @my_decorator
# def add(a, b):
#     return a + b
#
#
# add(1, 2)
# add(3, 2)
# add(5, 2)
#
#
# def my_decorator(func):
#     def inner(*args, **kwargs):
#         print(f"run {func.__name__} {args=} {kwargs=}")
#         return func(*args, **kwargs)
#
#     return inner
#
#
# @my_decorator
# def add(a, b):
#     return a + b
#
#
# @my_decorator
# def my_print(a):
#     return a * 5
#
# @my_decorator
# @my_decorator
# def my_sum(*args):
#     return sum(args)
#
#
# print(add(1, 2))
# print(my_print(1))
# print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(add(1, 2))
# print(my_print(1))
# print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(add(1, 2))
# print(my_print(1))
# print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def add(a, b):
    print(a + b)


add(1, 2)


@percent
@star
def add(a, b):
    print(a + b)


add(55, 2)
