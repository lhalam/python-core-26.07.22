#  Task 1
def divisor(num):
    for x in range(1, num + 1):
        if num / x == int(num / x):
            print(x)
            yield x
    while True:
        print('None')
        yield None

three = divisor(3)
next(three)
next(three)
next(three)

#  Task 2
# def logger(func):
#     def inner(*args, **kwargs):
#         if func.__name__ == 'print_arg':
#             res = func(*args, **kwargs)
#             print(f"Executing of function {func.__name__} with arguments "
#                   f"{0 if len(args)==0 else args}, second kwarg {0 if len(kwargs)==0 else kwargs}"
#                   .replace('(', '').replace(')', ''))
#             return res
#         print(f"Executing of function {func.__name__} with arguments "
#               f"{0 if len(args)==0 else args}, second kwarg {0 if len(kwargs)==0 else kwargs}"
#               .replace('(', '').replace(')', ''))
#         return func(*args, **kwargs)
#     return inner
#
#
# @logger
# def concat(*args, **kwargs):
#     result = ''
#     for el in args:
#         result += str(el)
#     for v in kwargs.values():
#         result += str(v)
#
#     return result
#
#
# @logger
# def sum(a, b):
#     return a + b
#
#
# @logger
# def print_arg(arg):
#     print(arg)
#
#
# print(concat(2, 3))
# print(concat('hello', 2))
# print(concat(first='one', second='two'))
# print(concat(1))
# print(concat('first string', second = 2, third = 'second string'))
# print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))
# print(sum(2, 3))
# dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
# concat(**dict_args)
# print_arg(2)


# Task 3
# from random import choice
#
#
# def randomWord(lists):
#     count = 0
#     while True:
#         result = choice(lists)
#         if result == lists[-1]:
#             print(f'Random == last array')
#             break
#         count += 1
#         print(f'{count} call of next(books) returns {result}')
#         yield result
#
#
# list = ['book', 'apple', 'word']
# books = randomWord(list)
# next(books)
# next(books)
# next(books)
# next(books)
