
class Animal:
    
    animals = dict()

    def __init__(self, name):
        self.name = name 

    def __call__(self, cls, *args, **kwargs):
        self.__class__.animals[self.name] = cls 


@Animal('dog')
class Dog:

    def say(self):
        return 'bark'


@Animal('cat')
class Cat:

    def say(self):
        return 'meow'


def main():
    print(Animal.animals['cat']().say())

if __name__ == '__main__':
    main()
