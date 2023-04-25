import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


print_name()


@start_end_decorator
def add4(x):
    return x + 4


# function has arguments
result = add4(10)
print(result)
print(help(add4))
print(add4.__name__)


# decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet('Alex')


@start_end_decorator
@repeat(num_times=4)
def say_hello(name):
    greeting = f'Hello hoooolaaalaaa {name}'
    print(greeting)
    return greeting


say_hello('Alex')
