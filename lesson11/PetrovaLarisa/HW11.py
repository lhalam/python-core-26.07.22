#Task 1


def divisor(num):
    for i in range(1, num//2+1):
        if num%i == 0:
            yield i
    else:
        while True:
            yield None
twenty = divisor(125)
print(next(twenty))
print(next(twenty))
print(next(twenty))
print(next(twenty))
print(next(twenty))
print(next(twenty))
print(next(twenty))

#Task 2
def logger(func):
   def inner(*a, **b):
       e = ""
       for i in a:
           e  += f'{i}, '
       for j in b:
           e += f"{b[j]}, "

       print(f"Executing of function {func.__name__} with arguments {e}...")

       return func(*a, **b)
   return inner

@logger
def concat(*a, **b):
    q = ''
    for r in a:
        q += str(r)
    for w in b:
        q += str(b[w])
    return q

@logger
def sum(a,b):
    return a+b

@logger
def print_arg(arg):
    print(arg)

print(concat(1))
print(concat(2, 3))
print(concat('first string', second = 2, third = 'second string'))
print(concat('first string', {'first kwarg' : 0, 'second kwarg': 'second kwarg'}))
print(sum(2, 3))
dict_args = {'first kwarg' : 0, 'second kwarg': 'second kwarg'}
print(concat(dict_args))
print_arg(2)

#Task 3
import random, copy
def randomWord(l):
    l_cur = copy.deepcopy(l)

    while True:
        if len(l_cur) == 1:
            yield l_cur[0]
            l_cur = copy.deepcopy(l)
        w = random.choice(l_cur)
        l_cur.remove(w)
        yield w

list = ['book', 'apple', 'word']
books = randomWord(list)
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))



