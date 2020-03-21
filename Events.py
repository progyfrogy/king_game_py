
"""
Authored by
kirprogfrog@gmail.com
"""

import random


class Event:
    """
    Every child of Event class has player
    variable(Player class) which sets in
    constructor (__init__ method)
    """
    player = None
    name = ""

    def __init__(self, player):
        print(self.name, "был создан")
        self.player = player

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
        self.player.decrease_carma(5)

    def no(self):
        self.player.increase_carma(5)
        self.player.decrease_money(100)

    def do_negative(self):
        pass

    def do_positive(self):
        pass

    def make(self):
        print("Горожане просят увеличения зарплат.")
        print("Повысить горожанам зарплаты?")
        print("Введите '1' если Да и '2' если Нет")

        a = self.get_player_choice()

        if a == 1:
            self.no()
        elif a == 2:
            self.yes()


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
            print(rand_int)
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

        player_choice = self.get_player_choice()

        if player_choice == 1:
            self.yes()
        else:
            self.no()


class EveryDayPayEvent(Event):
    everyday_pay = 0

    def show_cost(self):
        pass


class War(EveryDayPayEvent):
    everyday_pay = 25

    def show_cost(self):
        print("Война:", self.everyday_pay)

    def make(self):
        print("Началась война")
        print("Каждый ход с вашей казны будет поступать по 25 золота на содержание войск")
        self.player.increase_everyday_pay(self.everyday_pay)