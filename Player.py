"""
Authored by
kirprogfrog@gmail.com
"""
import os


class Player:
    _login = 'Kirill'
    _passed_days = 0
    _money = 1000
    _carma = 50
    _everyday_pay = 0

    instance = None

    # Синглтон
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    i = 1

    def save_score(self):
        print("Trying to find file", "score" + str(self.i) + ".txt")
        if os.path.exists("score" + str(self.i) + ".txt"):
            print("File score" + str(self.i) + ".txt was found, so testing score" + str(self.i + 1) + ".txt")
            self.i += 1
            self.save_score()
        else:
            print("File score" + str(self.i) + ".txt doesn't exist so we'll save score there")
            with open("score" + str(self.i) + ".txt", "w") as f:
                f.write(Player().get_login() + "\n" + "DAYS:" + str(Player().get_passed_days()) +
                        "\n" + "MONEY:" + str(Player().get_money()) + "\n" + "CARMA:" + str(Player().get_carma()))
                f.close()

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
            self.save_score()
            exit()
        else:
            self._money -= num
            print("Уменьшилось Золото(-", num, ")", sep='')
            print("Деньги:", self.get_money())

    def decrease_carma(self, num):
        if self._carma < num:
            print("Доверия вашего народа упало до 0. В скором времени произойдёт смена власти..")
            print("КОНЕЦ ИГРЫ")
            self.save_score()
            exit()
        else:
            self._carma -= num
            print("Уменьшилось Отношение(-", num, ")", sep='')
            print("Отношение:", self.get_carma())

    def increase_everyday_pay(self, val):
        self._everyday_pay += val

    def decrease_everyday_pay(self, val):
        self._everyday_pay -= val

    def pay_everyday_pay(self):
        self._money -= self._everyday_pay
        if self._everyday_pay > 0:
            print("С казны было списано", self._everyday_pay, "золота на ежедневные расходы")
            print("Деньги:", self.get_money())

    def get_money(self):
        return self._money

    def get_carma(self):
        return self._carma

    def get_passed_days(self):
        return self._passed_days

    def set_passed_days(self, val):
        self._passed_days = val

    def get_login(self):
        return self._login

    def set_login(self, val):
        self._login = val
