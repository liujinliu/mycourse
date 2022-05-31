# -*- coding: utf-8 -*-
import time
import threading

class Singleton:

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            time.sleep(1)
            self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]


@Singleton
class TestCls:
    pass


def task():
    print(id(TestCls()))


def main():
    for i in range(5):
        threading.Thread(target=task).start()
        # task()

if __name__ == '__main__':
    main()
