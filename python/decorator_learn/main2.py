
class Animal:
    
    animals = []

    def __init__(self, cls):
        self._cls = cls
        self.__class__.animals.append(cls)

    def __call__(self, *args, **kwargs):
        return self._cls(*args, **kwargs)


@Animal
class Dog:

    def say(self):
        return 'bark'


@Animal
class Cat:

    def say(self):
        return 'meow'


def main():
    for animal in Animal.animals:
        print(animal().say())

if __name__ == '__main__':
    main()
