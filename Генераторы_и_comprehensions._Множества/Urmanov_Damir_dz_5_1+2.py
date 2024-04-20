# 1
from itertools import islice


def my_gen(n):
    for i in range(1, n + 1, 2):
        yield i


gen = my_gen(15)
print(next(gen))
print(next(gen))
print(*islice(gen, 4))
print(sum(gen))


# 2
def my_gen(n):
    generator = (i for i in range(1, n + 1, 2))
    return generator


gen = my_gen(15)
print(next(gen))
print(next(gen))
print(*islice(gen, 3))
print(sum(gen))
