Cart = {
    "Apple": {'price': 35, 'quantity': 5},
    "Bread": {'price': 15, 'quantity': 8},
    "Tomato": {'price': 4, 'quantity': 25},
}
for item, info in Cart.items():
    total = info['price'] * info['quantity']
    print(f"{item}: Total = {total}")
total_price = 0
for item, info in Cart.items():
    total_price += info['price'] * info['quantity']

print(total_price)
print(len(Cart.keys()))
