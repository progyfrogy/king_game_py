"""
Authored by
kirprogfrog@gmail.com
"""

import sys
import time
import random

from Events import *
from Player import *
import os


# Test
def test():
    print("Стартую тест..")
    controller = GameController()
    print("")
    print("////////////////ИГРА НАЧАЛАСЬ////////////////")

    for i in range(0, 100):
        os.system("cls")

        print("")
        print("День:", i + 1, "7:00")
        print("")

        controller.delete_passed_events()

        if len(controller.active_everyday_pay_events) != 0:
            Player().pay_everyday_pay()

        controller.make_random_event()

        print("")
        print("День:", i + 1, "22:00")
        print("")

        Player().set_passed_days(i + 1)

        controller.increment_everyday_events()

        controller.start_command_cycle()


# Функция, определяющая есть ли определённый класс в списке
def is_class_in_list(active_events, wished):
    for obj in active_events:
        if type(obj) == type(wished):
            return True
    return False


# Функция, определяющая индекс класса в списке
def index_of_class_in_list(active_events: list, wished: object):
    for obj in enumerate(active_events):
        if type(obj[1]) == type(wished):
            return obj[0]
    return -1


class GameController:
    events = []
    active_everyday_pay_events = []
    everyday_pay_events = []

    def fill_events_list(self):
        # Создание игрока
        pl = Player()
        # Инициализация ивентов
        self.events.append(VulcanoEvent())
        self.events.append(RaidEvent())
        self.events.append(FestEvent())
        self.events.append(CitizensPaymentIncreaseEvent())
        self.events.append(DyingCitizenEvent())
        self.events.append(War())
        self.everyday_pay_events.append(War())
        self.events.append(RatsEvent())
        self.everyday_pay_events.append(RatsEvent())
        self.events.append(Chuma())
        self.everyday_pay_events.append(Chuma())

    def __init__(self):
        self.fill_events_list()
        # print(self.events)

    # Makes random event
    def make_random_event(self):
        random_event = self.events[random.randint(0, len(self.events) - 1)]
        """
        Если сгенерированный ивент является потомком класса
        EveryDayPayEvent и не находится в списке активных ивентов,
        то добавляем желаемый ивент в список активных, а иначе:
        
        Если сгенерированный ивент не является потомком класса
        EveryDayPayEvent, то просто запускаем, а иначе - рекурсивный вызов данной функции
        """
        if isinstance(random_event, EveryDayPayEvent) and not is_class_in_list(self.active_everyday_pay_events,
                                                                               random_event):
            self.active_everyday_pay_events.append(random_event)
            random_event.make()
        elif not isinstance(random_event, EveryDayPayEvent):
            random_event.make()
        else:
            self.make_random_event()

    def start_command_cycle(self):
        print("Посмотреть деньги в казне - money")
        print("Посмотреть отношение народа к королю - carma")
        print("Начать следующий день - next")
        print("Выйти из игры - exit")
        print("Посмотреть ежедневные расходы - everyday")

        if is_class_in_list(self.active_everyday_pay_events, War()):
            print("Посмотреть кол-во дней до окончания войны - days_of_war")

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
                if len(self.active_everyday_pay_events) == 0:
                    print("Нет ежедневных расходов")
                else:
                    print("Ежедневные расходы:")
                    for pay_event in self.active_everyday_pay_events:
                        pay_event.show_cost()
            elif inp == 'days_of_war':
                # Получаем активный War ивент(объект) из списка активных ивентов
                war_event = self.active_everyday_pay_events[
                    index_of_class_in_list(self.active_everyday_pay_events, War())]

                print("Кол-во дней до окончания войны: ", war_event.length - war_event.passed_days)
            elif inp == 'decrease_money':
                Player().decrease_money(1000)
            else:
                print("Не могу вас понять, ваше сиятельство")

    def delete_passed_events(self):
        for event in self.active_everyday_pay_events:
            if event.is_passed():
                self.active_everyday_pay_events.remove(event)
                event.say_last_words()
                Player().decrease_everyday_pay(event.everyday_pay)

    def increment_everyday_events(self):
        for event in self.active_everyday_pay_events:
            event.increment_passed_days()


# Call testing method
test()
