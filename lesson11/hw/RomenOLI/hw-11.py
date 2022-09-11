# 1. Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.

# def divisor(n):
#     for i in range(1, n+1):
#         if not (n % i):
#             print(i)
#             yield i
#     while True:
#         print("None")
#         yield None
#
# three = divisor(3)
# next(three)
# next(three)
# next(three)
# next(three)

# 2. Create decorator logger.
# The decorator should print to the console information about function's name and all its arguments separated with , for the function decorated with logger.
# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.

# def logger(func):
#     from functools import reduce
#     def inner(*args, **kwargs):
#         p = reduce(lambda x, y: str(x) + ", " + str(y), args, "") if args else ""
#         p += reduce(lambda x, y: str(x) + ", " + str(y), kwargs, "") if kwargs else ""
#         print(f"Executing of function {func.__name__} with arguments {p} ... ")
#         return func(*args, **kwargs)
#     return inner
#
# @logger
# def concat(*args, **kwargs):
#     from functools import reduce
#     try:
#         p = sum(args)
#         p += sum(kwargs)
#     except:
#         p = reduce(lambda x, y: str(x) + str(y), args, "") if args else ""
#         p += reduce(lambda x, y: str(kwargs[x]) + str(kwargs[y]), kwargs) if kwargs else ""
#     return p
#
# print(concat(2, 3))
# print(concat("Hello", 3))
# print(concat(first='one', second='two'))
# print(concat(1))
# print(concat('first string', second=2, third='second string'))
# print(concat('first string', {'first kwarg':0, 'second kwarg': 'second kwarg'}))

# 3. Generator function randomWord has as an argument list of words.
# It should return any random word from this list.
# Each time words are different until the end of the list is reached.
# Then words are taken from the initial list again.

# def randomWord(sp):
#     from random import randint
#     i = 0
#     dubl = sp.copy()
#     while i < len(sp):
#         r = randint(0, len(dubl)-1)
#         yield dubl[r]
#         dubl.remove(dubl[r])
#         i += 1
#     else:
#         i = 0
#         dubl = sp.copy()
#         yield dubl[randint(0, len(dubl)-1)]
#         dubl.remove(dubl[randint(0, len(dubl)-1)])
#
#
# ls = ['book', 'apple', 'word']
# books = randomWord(ls)
# print(next(books))
# print(next(books))
# print(next(books))
# print(next(books))
# print(next(books))