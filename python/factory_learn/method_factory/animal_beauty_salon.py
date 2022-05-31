from abc import ABC, abstractmethod
from service import HairDressing, Manicure, HaveShower, Massage

class BeautyPackage(ABC):

    def __init__(self):
        self.__services = []
        self.create_services()

    @abstractmethod
    def create_services(self):
        pass

    def add_service(self, service):
        self.__services.append(service)

    def list_services(self):
        return self.__services


class BP1(BeautyPackage):

    def create_services(self):
        self.add_service(HairDressing)
        self.add_service(Manicure)


class BP2(BeautyPackage):

    def create_services(self):
        self.add_service(HaveShower)
        self.add_service(Massage)


if __name__ == '__main__':
    bp_type = input('请输入选择的宠物美容套餐: ')
    bp = eval(bp_type.upper())()
    for s in bp.list_services():
        s().describle()
