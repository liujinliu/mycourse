# -*- coding: utf-8 -*-

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f'output from the __str__: name:{self.name}, '
                f'age:{self.age}')

    def __repr__(self):
        return (f'output from __repr__: name(self.name), '
               f'age(self.age)')

    def __format__(self, format_spec=''):
        if format_spec == '':
            return str(self)
        rs = format_spec.replace(
                '%name', self.name).replace('%age', f'{self.age}')
        return 'output from the __format__: ' + rs

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, v):
        return hash(self) == hash(v)


if __name__ == '__main__':
    a = set()
    a.add(Person('Tom', 22))
    a.add(Person('Tom', 22))
    print(len(a))
