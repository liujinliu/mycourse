from abc import ABC, abstractmethod

class TourPlanTemplate(ABC):
    """这是一个模板类
       run函数描述了一个旅行计划
          chose_transport负责设计旅行交通工具
          day0描述旅行第一天的计划
          day1描述旅行第二天的计划
          day2描述旅行第三天的计划
    """

    @abstractmethod
    def chose_transport(self):
        pass

    @abstractmethod
    def day0(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    def __create_bill(self):
        print('create bill.....')

    def run(self):
        print('交通方式: ', end='')
        self.chose_transport()
        print('第1天: ', end='')
        self.day0()
        print('第2天: ', end='')
        self.day1()
        print('第3天: ', end='')
        self.day2()
        self.__create_bill()

