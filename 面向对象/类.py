class Coffee:
    water = 0
    milk = 0

    def add_water(self):
        self.water += 1
        self.hotwater = 1


mocha = Coffee()
mocha.add_water()


# print(mocha.water)


class Father:
    def run(self):
        print("run in father")


class Son(Father):
    def run(self):
        # super().run()
        print('child run')


son1 = Son()


# son1.run()


class Animal:

    def eat(self, some):
        print(some)

    def run(self):
        print("1")


class Mouse(Animal):
    def eat(self):
        print(Mouse.__name__)
        super().eat("偷吃")


mouse = Mouse()
mouse.eat()
