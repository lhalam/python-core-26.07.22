"Task 1"

def divisor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            yield i
    while 1:
        print(None)
        yield None


eight = divisor(8)


# next(eight);next(eight);next(eight);next(eight);next(eight);next(eight)

"Task 2"

def logger(func):
    def inner(*args, **kwargs):
        print(f'Executing of <{func.__name__}> with arguments: ', end='')
        print(*args, *[_ for _ in kwargs.values()])
        return func(*args, **kwargs)

    return inner

@logger
def concat(*args, **kwargs):
    concat_string = ''
    for i in args:
        concat_string += str(i)
    for key, value in kwargs.items():
        concat_string += str(value)
    return concat_string


@logger
def summary(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)

# print(concat(2, 3))
# print(concat('hello', 2))
# print(concat(first='one', second='two'))
# print(concat("first string", second=2, third='second string'))
# print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))
# dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
# concat(**dict_args)
# print(summary(2, 3))
# print_arg(2)

'Task 3'
import random as r
words_list = ['book', 'apple', 'word']

def randomWord(collection):

    while True:
        print(r.choice(collection))
        yield r.choice(collection)

l = randomWord(words_list)

# next(l);next(l);next(l);next(l);next(l)

