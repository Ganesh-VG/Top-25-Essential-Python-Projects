class Coffee_Maker():
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.cost = 0

    def report(self):
        print(f"water : {self.water}\n milk : {self.milk}\n coffee : {self.coffee} \n cost : {self.cost}")



    def resource_check(self,gen):
        if self.water > gen.water and self.milk > gen.milk and  self.coffee > gen.coffee:
           return True
        else:
            print("Sorry, resource is insufficient")
            return False

    def coffee_machine(self,gen):
        print("Please have your coffee")
        self.water -= gen.water
        self.milk -= gen.milk
        self.coffee -= gen.coffee


