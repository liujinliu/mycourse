from tour_plan_adult import TourPlanForAdult
from tour_plan_children import TourPlanForChild


all_tour_plan = {
        'child': TourPlanForChild,
        'adult': TourPlanForAdult
    }

def main():
    plan = input('请选择旅游计划类型(child/adult): ')
    all_tour_plan[plan]().run()


if __name__ == '__main__':
    main()

