class UnitValue:

    def __init__(self, unit):
        self.value = None
        self.unit = unit

    def __set__(self, instance, value):
        print('SET:', instance, value)
        with open('tmp.value','w') as f:
            f.write(f'{value}')
        self.value = value

    def __get__(self, instance, owner):
        print('GET: ', instance, owner)
        return f'{self.value}-{self.unit}'


class TestClass:

    n = UnitValue('km')


if __name__ == '__main__':
    t1 = TestClass()
    t1.n = 1
    print(t1.n)

