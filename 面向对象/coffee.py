"""
 练习: 开发自动咖啡机
 分析:
  1. 调配各种类型的咖啡需要咖啡原液、水、牛奶 三种原料
  2.三种原料根据不同比例、属性叠加形成新的咖啡品类
  3. 需在开发时交付后端接口
"""

""" 
定义属性和方法
① 咖啡成品有冷、热的差别，因为水、牛奶需要冷热属性
② 三种原料都需要添加，因为需要添加方法
③ 三种原料的单位不同，咖啡液以份数为单位，水和牛奶以毫升为单位
"""


class WaterMixin:

    def __init__(self):
        self.temperature = None
        self.volume = 0

    def add_water(self, temp, vol):
        self.volume = vol
        if temp == 'hot':
            self.temperature = 'hot'
        elif temp == 'cold':
            self.temperature = 'cold'

        return f"add{self.temperature} water {self.volume} ML"


class CoffeeMixin:

    def __init__(self):
        self.numbers = None

    def add_coffee(self, numbers):
        self.numbers = numbers
        return f"add coffee {self.numbers}"


class MilkMixin:
    def __init__(self):
        self.temperature = None
        self.volume = None

    def add_milk(self, temp, vol):
        self.volume = vol
        if temp == 'hot':
            self.temperature = 'hot'
        elif temp == 'cold':
            self.temperature = 'cold'

        return f"add{self.temperature} milk {self.volume} ML"


class Cof(WaterMixin, CoffeeMixin, MilkMixin):

    def __init__(self, water=-1, water_temp='cold', milk=-1, milk_temp='cold', coffee=0):
        self.water = water
        self.water_temp = water_temp
        self.milk = milk
        self.milk_temp = milk_temp
        self.coffee = coffee
        self.prescription = []

        if int(water) > 0:
            water_desc = super().add_water(self.water_temp, self.water)
            self.prescription.append(water_desc)

        if int(self.milk) > 0:
            milk_desc = super().add_milk(self.milk_temp, self.milk)
            self.prescription.append(milk_desc)

        if int(self.coffee) > 0:
            coffer_desc = super().add_coffee(self.coffee)
            self.prescription.append(coffer_desc)

    def printPrescription(self):
        for i in self.prescription:
            print(i)


icano_coffer = Cof(water=150, milk=50, coffee=-1)
icano_coffer.printPrescription()
