import random
MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
day = 1
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while price>= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1+price_change)
    print("On day {} price is: ${:,.2f}".format(day,price))
    day = day + 1
print("Final price is: ${:,.2f}!".format(price))

