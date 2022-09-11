import random

# Task 1

def divisor(x):
    count = 1
    while count <= x:
        if x % count == 0:
            yield count
            count += 1
        else:
            count += 1
    while True:
        yield None

g = divisor(4)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Task 2

def logger(func):
    def inner(*args, **kwargs):
        ar = ''
        for i in args:
            ar += f'{i}, '
        for j in kwargs:
            ar += f'{kwargs[j]}, '
        print(f"func_name {func.__name__} {ar} ")
        return func(*args, **kwargs)

    return inner


@logger
def concat(*args, **kwargs):
    ar_2 = ''
    for k in args:
        ar_2 += f'{k}'
    for h in kwargs:
        ar_2 += f'{kwargs[h]}'
    return ar_2


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


print(concat(1))
print(concat('first string', second=2, third='second string'))
print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))
print(sum(2, 3))
dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
print(concat(**dict_args))
print_arg(2)

# Task 3

def randomWord(list_1):
    while True:
        a = random.randint(0, len(list_1) - 1)
        yield list_1[a]


g = randomWord(['book', 'apple', 'word'])
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
