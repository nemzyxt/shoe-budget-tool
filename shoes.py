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

    def buy(self, budget):
        self.budget_check(budget)

        if budget >= self.price:
            print(f"You can get some {self.name}")
            if budget == self.price:
                print("You have exact money for the shoes")
            else:
                print(f"""You can get the shoes and have a
                change of {self.change(budget)}""")

        exit("Thanks for using our Shoe Budget App :)")
