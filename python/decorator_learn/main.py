import functools

def my_decorator(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('hello from decorator')
        return func(*args, **kwargs)
    return inner


@my_decorator
def test(name):
    print(name)


if __name__ == '__main__':
    test('anan')
    print(test.__name__)
