# 1. Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.
def divisor(n):
    for i in range(1, n+1):
        if not (n % i):
            print(i)
            yield i
    else:
        print("None")
        yield None

three = divisor(5)
next(three)
next(three)
next(three)
# next(three)
