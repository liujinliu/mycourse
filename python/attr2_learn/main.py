class Duck:

    def __init__(self, name, age):
        self._name = name
        self.age = age
        self.__name = name


if __name__ == '__main__':
    d = Duck('tom', 1)
    print(d._Duck__name) 
