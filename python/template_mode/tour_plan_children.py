from tour_plan_template import TourPlanTemplate

class TourPlanForChild(TourPlanTemplate):

    def chose_transport(self):
        print('乘坐地铁')

    def day0(self):
        print('去动物园')

    def day1(self):
        print('去天文馆')

    def day2(self):
        print('去欢乐谷')
