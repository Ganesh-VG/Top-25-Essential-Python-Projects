class Menu_Store():
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

class Menu():
    def __init__(self):
        self.name = [
            Menu_Store(name="espresso", water=100, milk=75, coffee=20, cost=10),
            Menu_Store(name="latte", water=75, milk=50, coffee=25, cost=15),
            Menu_Store(name="cappuccino", water=120, milk=100, coffee=18, cost=20)
        ]

    def data(self,data):
        for item in self.name:
            if item.name == data:
                return item



