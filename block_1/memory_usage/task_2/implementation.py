import gc
import sys

class MyObject:
    instance = 0

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        MyObject.instance += 1
        self.count = MyObject.instance


def cache(func):
    """
    Обертка, кэширующая результат.
    """
    cached = {}
    func._cache = cached

    def wrapped(*args):
        nonlocal cached
        if not cached.get(args):
            result = func(*args)
            cached[args] = result
            return result
        else:
            return cached[args]
    return wrapped


@cache
def create_object(name):
    create_object._cache = name
    return MyObject(name)


print(MyObject.instance)
aaa = create_object('A')
print(MyObject.instance)
create_object('B')
print(MyObject.instance)

print(dir(create_object))
