# Task 1

Create function-generator `divisor` that should return all divisors of the positive number.

If there are no divisors left function should return `None`.

```python
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None
```

# Task 2

Create decorator `logger`. The decorator should print to the console information about function's name and all its arguments separated with `,` for the function decorated with `logger`.

Create function `concat` with any numbers of any arguments which concatenates arguments and apply `logger` decorator for this function. 

```python
# type your code 

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
```


For example
```python
print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
```

| Test |                            Expected                            |
|---|--------------------------------------------------------|
| `print(concat(1))` | Executing of function concat with arguments 1... <br>1 |
| `print(concat('first string', second = 2, third = 'second string'))` | Executing of function concat with arguments first string, 2, second string...<br>first string2second string |
| `print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))` | Executing of function concat with arguments first string, {'first kwarg': 0, 'second kwarg': 'second kwarg'}... <br>first string{'first kwarg': 0, 'second kwarg': 'second kwarg'} |
| `print(sum(2,3))` | Executing of function sum with arguments 2, 3...<br>5 |
| `dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}<br>concat(**dict_args)` | Executing of function concat with arguments 0, second kwarg... |
| `print_arg(2)` | 2<br>rExecuting of function print_arg with arguments 2... |

# Task 3

Generator function `randomWord` has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. Then words are taken from the initial list again.


For example if 
```python
list = ['book', 'apple', 'word']

books = randomWord(list)

then possible output example 

first call of next(books) returns apple

second call of next(books) returns book

third call of next(books) returns word

fourth call of next(books) returns book
```