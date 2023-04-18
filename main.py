from shoes import Shoes

low = Shoes("Cheaps Lit", 30)
medium = Shoes("Air Force 1", 120)
high = Shoes("Lof Whites", 400)

try:
    shoe_budget = float(input("What is your shoe budget ?"))
except ValueError:
    exit("Kindly provide a number as input")

for shoe in [high, medium, low]:
    shoe.buy(shoe_budget)
