# Task 1

def divisor(num):
    i = 0
    while num>=i:
        i += 1
        if num%i==0:
            yield i
        if i >= num:
            yield "none"

g = divisor(3)
print(next(g))
print(next(g))
print(next(g))

# Task 2
def logger(func):
    def inner(*args, **kwargs):
        print(f"Executing of {func.__name__} with arguments ",  end='')
        print(*args, sep=", ", end='')
        for k, v in kwargs.items():
            print(f', {v}', end='')
        print()
        return func(*args, **kwargs)

    return inner

@logger
def concat(*args, **kwargs):
    a = ""
    for i in args:
        a = a+str(i)
    for k, v in kwargs.items():
        a = a+str(v)
    return a


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


print(concat(2, 3))
print(concat('hello', 2))
print(concat (first = 'one', second = 'two'))
print(concat('first string', second = 2, third = 'second string'))
print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))
dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)
print(sum(2,3))
print_arg(2)

# Task 3

import random
def fruit():
    while True:
        color = ['book', 'apple', 'word']
        yield random.choice(color)
k = fruit()
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))


