from src import TestCase


def logger(fn):
    def wrapper(*args, **kwargs):
        try:
            fn(*args, **kwargs)
            print(f"{fn.__name__} success")
        except AssertionError as AssError:
            print(f"{fn.__name__} {AssError}")

    return wrapper


@TestCase.title('Add to numbers')
@logger
def add(a, b):
    sum = a + b
    assert sum == 5, "Failed"
    return sum


add(2, 3)
