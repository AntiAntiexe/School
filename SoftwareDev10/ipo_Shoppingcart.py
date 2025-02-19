price = int(input("Price of item: "))
quantity = int(input("Quantitiy of item: "))
x = True
prices = []
quantities = []
while x:
    prices.append(price)
    quantities.append(quantity)
    try:
        price = int(input("Price of item: "))
        quantity = int(input("Quantitiy of item: "))
    except ValueError:
        x = False

total = []
for i in range(len(prices)):
    total.append(prices[i] * quantities[i])

withTax = []
for i in total:
    withTax.append(i * 1.1)


print(f"Your total {sum(withTax)}")

if sum(withTax) == 20:
    print("Too expensive")
