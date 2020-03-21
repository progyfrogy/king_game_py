"""
Authored by
kirprogfrog@gmail.com
"""

import sys
import time
import random

from Events import *
from Player import *


# Test
def test():
    print("Стартую тест..")
    controller = GameController()
    print("")
    print("////////////////ИГРА НАЧАЛАСЬ////////////////")

    for i in range(0, 100):
        print("")
        print("День:", i + 1, "7:00")
        print("")
        Player().pay_everyday_pay()
        controller.make_random_event()

        print("")
        print("День:", i + 1, "22:00")
        print("")
        print("Посмотреть деньги в казне - money")
        print("Посмотреть отношение народа к королю - carma")
        print("Начать следующий день - next")
        print("Выйти из игры - exit")
        print("Посмотреть ежедневные расходы - everyday")
        # command cycle
        while True:
            inp = input()
            if inp == 'money':
                print("Деньги:", Player().get_money())
            elif inp == 'carma':
                print("Отношение:", Player().get_carma())
            elif inp == 'next':
                break
            elif inp == 'exit':
                print("КОНЕЦ ИГРЫ")
                exit()
            elif inp == 'want_some_money':
                print("Чит на деньги использован(+1000 золота)")
                print("Достижения недоступны")
                Player().increase_money(1000)
            elif inp == 'everyday':
                if len(controller.active_everyday_pay_events) == 0:
                    print("Нет ежедневных расходов")
                else:
                    print("Ежедневные расходы:")
                    for pay_event in controller.active_everyday_pay_events:
                        pay_event.show_cost()
            else:
                print("Не могу вас понять, ваше сиятельство")


# Функция, определяющая есть ли определённый класс в списке
def is_class_in_list(active_events, wished):
    for obj in active_events:
        if type(obj) == type(wished):
            return True
    return False


class GameController:
    events = []
    active_everyday_pay_events = []
    everyday_pay_events = []

    def fill_events_list(self):
        # Создание игрока
        pl = Player()
        # Заполняем массив ивентов
        self.events.append(VulcanoEvent(pl))
        self.events.append(RaidEvent(pl))
        self.events.append(FestEvent(pl))
        self.events.append(CitizensPaymentIncreaseEvent(pl))
        self.events.append(DyingCitizenEvent(pl))
        self.events.append(War(pl))
        self.everyday_pay_events.append(War(pl))

    def __init__(self):
        self.fill_events_list()
        # print(self.events)

    # Makes random event
    def make_random_event(self):
        random_event = self.events[random.randint(0, len(self.events) - 1)]
        """
        Если сгенерированный ивент является потомком класса
        EveryDayPayEvent и не находится в списке активных ивентов,
        то добавляем желаемый ивент в список активных
        """
        if isinstance(random_event, EveryDayPayEvent) and not is_class_in_list(self.active_everyday_pay_events,
                                                                               random_event):
            self.active_everyday_pay_events.append(random_event)
            random_event.make()
        """
        Если сгенерированный ивент не является потомком класса
        EveryDayPayEvent, то просто запускаем, а иначе - ничего не делаем
        """
        if not isinstance(random_event, EveryDayPayEvent):
            random_event.make()


# Call testing method
test()
