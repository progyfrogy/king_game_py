
"""
Authored by
kirprogfrog@gmail.com
"""


class Player:
    _money = 1000
    _carma = 50
    _everyday_pay = 0

    instance = None

    # Синглтон
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def increase_money(self, num):
        self._money += num
        print("Увеличилось Золото(+", num, ")", sep='')
        print("Деньги:", self.get_money())

    def increase_carma(self, num):
        self._carma += num
        print("Увеличилось Отношение(+", num, ")", sep='')
        print("Отношение:", self.get_carma())

    def decrease_money(self, num):
        if self._money < num:
            print("Нет золота БАН")
            print("КОНЕЦ ИГРЫ")
            exit()
        else:
            self._money -= num
            print("Уменьшилось Золото(-", num, ")", sep='')
            print("Деньги:", self.get_money())

    def decrease_carma(self, num):
        if self._carma < num:
            print("Доверия вашего народа упало до 0. В скором времени произойдёт смена власти..")
            print("КОНЕЦ ИГРЫ")
            exit()
        else:
            self._carma -= num
            print("Уменьшилось Отношение(-", num, ")", sep='')
            print("Отношение:", self.get_carma())

    def increase_everyday_pay(self, val):
        self._everyday_pay += val

    def pay_everyday_pay(self):
        self._money -= self._everyday_pay
        if self._everyday_pay > 0:
            print("С казны было списано", self._everyday_pay, "золота на ежедневные расходы")
            print("Деньги:", self.get_money())

    def get_money(self):
        return self._money

    def get_carma(self):
        return self._carma
