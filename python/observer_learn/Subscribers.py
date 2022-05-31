# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass


class Subscriber01(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher 
        publisher.attach(self)

    def update(self):
        print(self.__class__.__name__, ':', self.publisher.get_news())


class Subscriber02(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher 
        publisher.attach(self)

    def update(self):
        print(self.__class__.__name__, ':', self.publisher.get_news())


class Subscriber03(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher 
        publisher.attach(self)

    def update(self):
        print(self.__class__.__name__, ':', self.publisher.get_news())

