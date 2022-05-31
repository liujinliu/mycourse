from abc import ABC, abstractmethod

class Service(ABC):

    @abstractmethod
    def describle(self):
        pass


class HairDressing(Service):

    def describle(self):
        print('welcome to have hairdressing')


class Manicure(Service):

    def describle(self):
        print('welcome to have manicure')


class HaveShower(Service):

    def describle(self):
        print('welcome to have shower')


class Massage(Service):

    def describle(self):
        print('welcome to have massage')
