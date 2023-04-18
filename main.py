class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def budget_check(self, budget):
        if not isinstance(budget, (int, float)):
            print("Invalid entry. Kindly provide a number")
            exit()

    def change(self, budget):
        return (budget - self.price)
    
    