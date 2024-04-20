from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        numbers = [i for i in args]
        n = [f'{func.__name__}({i}: {type(i)})' for i in numbers]
        print(*n, *func(*args), sep='\n')
        print(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    numbers = [i for i in args if isinstance(i, int) or isinstance(i, float)]
    print(numbers)
    return [n ** 3 for n in numbers]


calc_cube(4, 'str', {'int': 23}, 3.23, ('tuple', 4), [2, 43], {2, 43})
