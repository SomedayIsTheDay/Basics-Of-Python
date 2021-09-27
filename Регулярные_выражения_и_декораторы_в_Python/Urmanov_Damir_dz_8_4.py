from functools import wraps


def val_checker(lambda_func):
    def val_check(func):
        @wraps(func)
        def wrapper(number):
            if lambda_func(number):
                print(func(number))
            else:
                raise ValueError(f'wrong number {number}')
        return wrapper
    return val_check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube('asd')
except (ValueError, TypeError) as e:
    print(e)
