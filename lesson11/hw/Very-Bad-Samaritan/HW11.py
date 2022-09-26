from random import randint

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


# g = divisor(15)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# Task 2


def logger(func):
    def inner(*args, **kwargs):
        if func.__name__ == 'print_arg':
            res = func(*args, **kwargs)
            print(f"Executing of function {func.__name__} with arguments "
                  f"{0 if len(args)==0 else args}, second kwarg {0 if len(kwargs)==0 else kwargs}"
                  .replace('(', '').replace(')', ''))
            return res
        print(f"Executing of function {func.__name__} with arguments "
              f"{0 if len(args)==0 else args}, second kwarg {0 if len(kwargs)==0 else kwargs}"
              .replace('(', '').replace(')', ''))
        return func(*args, **kwargs)
    return inner


@logger
def concat(*args, **kwargs):
    result = ''
    for el in args:
        result += str(el)
    for v in kwargs.values():
        result += str(v)

    return result


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


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


def randomWord(sp):
    i = 0
    dubl = sp.copy()
    while i < len(sp):
        r = randint(0, len(dubl)-1)
        yield dubl[r]
        dubl.remove(dubl[r])
        i += 1
    else:
        i = 0
        dubl = sp.copy()
        yield dubl[randint(0, len(dubl)-1)]
        dubl.remove(dubl[randint(0, len(dubl)-1)])


ls = ['book', 'apple', 'word']
books = randomWord(ls)
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))



# Чесне слово, я поняття не маю, чому видає "StopIteration", я не знаю, як це пофіксити. Тут мої повноваження всьо
