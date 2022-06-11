class MyObject:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


def cache(func):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv

    return wrapper


@cache
def create_object(name):
    return MyObject(name)
