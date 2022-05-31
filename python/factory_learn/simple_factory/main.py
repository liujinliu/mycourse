# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Animal(ABC):
   
    @abstractmethod
    def say(self):
        pass


class Dog(Animal):

    def say(self):
        print('bark bark')


class Cat(Animal):

    def say(self):
        print('meow meow')


class AnimalFactory:

    __animal = {'dog': Dog, 'cat': Cat}

    @classmethod
    def instance(cls, animal_type):
        return cls.__animal[animal_type]()



if __name__ == '__main__':
    AnimalFactory.instance('cat').say()

