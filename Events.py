"""
kirprogfrog@gmail.com
Authored by
"""

import random
from Player import *


class Event:
    """
    Every child of Event class has player
    variable(Player class) which sets in
    constructor (__init__ method)
    """
    player = Player()
    name = ""

    def __init__(self):
        # print(self.name, "был создан")
        pass

    def make(self):
        pass


class VulcanoEvent(Event):
    name = "Vulcano Event"

    def make(self):
        print("Ваш город был подвержен извержению вулкана(-100 золота)")
        self.player.decrease_money(100)


class RaidEvent(Event):
    name = "Raid Event"

    def make(self):
        print("Ваш город был подвержен атаке рейдеров(-200 золота)")
        self.player.decrease_money(200)


class FestEvent(Event):
    name = "Money Fest Event"

    def make(self):
        print("В городе прошёл Фестиваль Денег(+300 золота)")
        self.player.increase_money(300)


class ChoiceEvent(Event):
    """
    Event interface with a choice
    """

    def get_player_choice(self):
        while True:
            try:
                a = int(input())
                if a == 1 or a == 2:
                    return a
                else:
                    print("Введите 1 или 2")
            except:
                print("Введите 1 или 2")

    def do_yes_or_no(self):
        a = self.get_player_choice()

        if a == 1:
            self.yes()
        elif a == 2:
            self.no()

    def yes(self):
        pass

    def no(self):
        pass

    def do_negative(self):
        pass

    def do_positive(self):
        pass

    def make(self):
        pass


class CitizensPaymentIncreaseEvent(ChoiceEvent):

    def yes(self):
        self.player.increase_carma(5)
        self.player.decrease_money(100)

    def no(self):
        self.player.decrease_carma(5)

    def do_negative(self):
        pass

    def do_positive(self):
        pass

    def make(self):
        print("Горожане просят увеличения зарплат.")
        print("Повысить горожанам зарплаты?")
        print("Введите '1' если Да и '2' если Нет")

        self.do_yes_or_no()


class DyingCitizenEvent(ChoiceEvent):

    def do_negative(self):
        print("Горожанин протягивает вам руку и говорит:")
        print("'я съел деда'")
        self.player.decrease_money(100)
        pass

    def do_positive(self):
        print("Горожанин протягивает вам руку и говорит:")
        print("Вот тебе золото, мне оно уже не нужно..")
        self.player.increase_money(100)
        pass

    def yes(self):
        self.player.increase_carma(5)
        rand_int = random.randint(0, 10)

        ''' 40% на неудачу '''
        if rand_int == 0 or rand_int == 1 or rand_int == 2 or rand_int == 3:
            print("Неудача")
            self.do_negative()
        else:
            print("Удача")
            self.do_positive()

    def no(self):
        self.player.decrease_carma(5)

    def make(self):
        print("Вы видите умирающего горожанина на дороге.")
        print("Помочь горожанину?")
        print("Введите '1' если Да и '2' если Нет")

        self.do_yes_or_no()


class EveryDayPayEvent(Event):
    everyday_pay = 0
    min_length = 0
    max_length = 0
    passed_days = 0
    length = 0

    name = "Every Day Pay Event"

    def __init__(self):
        super().__init__()
        self.length = random.randint(self.min_length, self.max_length)

    def show_cost(self):
        pass

    def is_passed(self):
        if self.passed_days == self.length:
            return True
        else:
            return False

    def increment_passed_days(self):
        self.passed_days += 1

    def say_last_words(self):
        pass


class War(EveryDayPayEvent):
    everyday_pay = 25
    min_length = 10
    max_length = 18
    passed_days = 0
    length = 0

    name = "War"

    def __init__(self):
        super().__init__()

    def show_cost(self):
        print("Война:", self.everyday_pay, "золота в день")

    def make(self):
        print("Началась война:", self.length, "дней")
        print("Каждый ход с вашей казны будет поступать по", self.everyday_pay, "золота на содержание войск")
        self.player.increase_everyday_pay(self.everyday_pay)

    def say_last_words(self):
        print("Война закончилась!")


class RatsEvent(EveryDayPayEvent):
    everyday_pay = 10
    min_length = 3
    max_length = 7
    passed_days = 0
    length = 0

    name = "Rats In Warehouse"

    def __init__(self):
        super().__init__()

    def show_cost(self):
        print("Крысы на складе:", self.everyday_pay, "золота в день")

    def make(self):
        print("Завелись крысы на складе!:", self.length, "дней")
        print("Каждый ход с вашей казны будет поступать по", self.everyday_pay, "золота на покупки химикатов")
        self.player.increase_everyday_pay(self.everyday_pay)

    def say_last_words(self):
        print("Крысы на складе вымерли!")


class Chuma(EveryDayPayEvent):
    everyday_pay = 5
    min_length = 20
    max_length = 30
    passed_days = 0
    length = 0

    name = "Every Day Pay Event"

    def __init__(self):
        super().__init__()

    def show_cost(self):
        print("Чума в государстве:", self.everyday_pay, "золота в день")

    def make(self):
        print("Торговый караван, прибывший в город занёс какую-то заразу!:", self.length, "дней")
        print("Каждый ход с вашей казны будет поступать по", self.everyday_pay, "золота на покупку лекарств")
        self.player.increase_everyday_pay(self.everyday_pay)

    def say_last_words(self):
        print("Чума закончилась!")
