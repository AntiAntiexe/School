import datetime

# Define the prices for each coffee size
SMALL_PRICE = 4.80
MEDIUM_PRICE = 5.50
LARGE_PRICE = 6.50
# Define the discount rate for concession card holders
CONCESSION_DISCOUNT_RATE = 0.25
# Define the discount for every 4 coffees
COFFEE_DISCOUNT = 3.0
# Define the file name for sales data
SALES_FILE_NAME = "sales.txt"
# Complete this function (10 marks)



def apply_concession_discount(total_cost):
    has_concession_card = input("Do you have a concession card? (yes or no) ").lower()
    if has_concession_card == "yes":
        total_cost = total_cost * (1 - CONCESSION_DISCOUNT_RATE)
    elif has_concession_card == "no":
        total_cost = total_cost

    return total_cost, has_concession_card


# Complete this function (25 marks)
def get_order():
    num_coffees = int(input("How many coffees would you like to order? "))
    total_cost = 0.0
    for i in range(num_coffees):
        coffee_size = input("Enter the size of coffee " + "#"+ str(i) + " (small, medium, large) ").lower()
        if coffee_size == "small":
            total_cost += SMALL_PRICE
        elif coffee_size == "medium":
            total_cost += MEDIUM_PRICE
        elif coffee_size == "large":
            total_cost += LARGE_PRICE
        else:
            print("Invalid size. Please enter small, medium, or large.")
            continue
    return total_cost, num_coffees


# Complete this function (20 marks)
def apply_coffee_discount(total_cost, num_coffees):
    if total_cost %
        num_discounts = num_coffees // 4
        total_cost -= num_discounts * COFFEE_DISCOUNT
    return total_cost

def display_total_cost(total_cost):
    print(f"Your total cost is ${total_cost:.2f}")
    # Display the total cost to the user

def save_sale_data(total_cost, has_concession_card):
    # Save the sale data to a file
    sale_data = {
        "time": str(datetime.datetime.now()),
        "sale": round(total_cost, 2),
        "concession": "yes" if has_concession_card else "no",
    }

    with open(SALES_FILE_NAME, "a") as sales_file:
        sales_file.write(str(sale_data) + "\n")


def main():
    # Get the order details from the user
    total_cost, num_coffees = get_order()
    # Apply the concession discount if applicable
    total_cost, has_concession_card = apply_concession_discount(total_cost)
    # Apply the coffee discount if applicable
    total_cost = apply_coffee_discount(total_cost, num_coffees)
    # Save the sale data to a file
    save_sale_data(total_cost, has_concession_card)
    # Display the total cost to the user
    display_total_cost(total_cost)


if __name__ == "__main__":
    main()
