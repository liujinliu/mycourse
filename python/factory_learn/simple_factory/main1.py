# -*- coding: utf-8 -*-
import functools
from abc import ABC, abstractmethod


class Animal(ABC):
   
    @abstractmethod
    def say(self):
        pass


class AnimalFactory:

    __animal = {}

    @classmethod
    def instance(cls, animal_type):
        return cls.__animal[animal_type]()

    @classmethod
    def register(cls, animal_type: str,
                 animal_cls: Animal):
        cls.__animal[animal_type] = animal_cls


def animal_register(animal_type):

    def wrapper(cls):
        AnimalFactory.register(animal_type, cls)
        @functools.wraps(cls)
        def inner(*args, **kwargs):
            return cls(*args, **kwargs)
        return inner
    return wrapper


@animal_register('dog')
class Dog(Animal):

    def say(self):
        print('bark bark')


@animal_register('cat')
class Cat(Animal):

    def say(self):
        print('meow meow')


if __name__ == '__main__':
    AnimalFactory.instance('cat').say()

