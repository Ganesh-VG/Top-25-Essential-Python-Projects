from menu import Menu

class Coins:
    def __init__(self, cost):
        self.cost = cost.cost

    def input_coins(self):
        print("please insert coins")
        total = int(input("no. of fives\n")) * 5 + int(input("no. of twos\n")) * 2 + int(input("no. of ones\n")) * 1
        if total >= self.cost:
            change = total - self.cost
            print(f"Please collect your change of {change}")
            return True
        if total < self.cost:
            print("Insufficient balance")
            return False
