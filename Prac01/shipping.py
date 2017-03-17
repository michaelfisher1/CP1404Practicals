number_of_items = (int(input("How many items do you wish to ship?")))
total_cost = 0
while number_of_items < 0:
    print("Invalid Number of items")
    number_of_items = (int(input("How man items do you wish to ship?")))
for i in range(number_of_items):
    item_price = int(input("Price of item"))
    while item_price < 0:
        item_price = int(input("Invalid price, please enter correct price."))
    total_cost = total_cost + item_price
if total_cost > 100:
    adjusted_total = total_cost - (total_cost * .10)
    print("Total shipping cost is:", adjusted_total)
else:
    print(total_cost)


