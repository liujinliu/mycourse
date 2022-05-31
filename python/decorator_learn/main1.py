import functools

def my_decorator(greeting):

    def wraper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print('hello from decorator:' + greeting)
            return func(*args, **kwargs)
        return inner
    return wraper


@my_decorator('how are you')
def test(name):
    print(name)


if __name__ == '__main__':
    test('anan')
    # print(test.__name__)
