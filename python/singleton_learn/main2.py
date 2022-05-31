# -*- coding: utf-8 -*-
import threading


class Singleton:
    __instance_lock = threading.Lock()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__instance_lock:
                if not cls.__instance:
                    cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class TestCls(Singleton):
    pass


def task():
    print(id(TestCls()))


def main():
    for i in range(5):
        threading.Thread(target=task).start()

if __name__ == '__main__':
    main()
