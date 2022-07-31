class Money:
    def __init__(self, money):
        self.__money = money
    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
    def get_money(self):
        return self.__money
    def add_money(self, mn):
        if self.__check_money(mn.get_money()):
            self.__money += mn.get_money()


    @classmethod
    def __check_money(cls, money):
        return isinstance(money, int) and 0 <= money

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
print(m1)
print(m2)