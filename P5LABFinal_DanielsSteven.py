# Steven Daniels
# 7/23/2024
# P5 Final Project
# Python FInal Project

def show_avail_items(items):
    item_list = sorted(items.keys())
    
    header = "{:<20} {:<15}".format('Grocery Item', 'Price')
    separator_line = '-' * len(header)
    
    print(header)
    print(separator_line)
    
    for item in item_list:
        price = items.get(item, 0)
        formatted_price = f"${price:.2f}"
        print("{:<20} {:<15}".format(item, formatted_price))
    
    print(separator_line)

def add_items_to_cart(items):
    cart = []
    print("\n*Welcome to the Grocery Checkout*\n")
    
    while True:
        user_input = input("Enter an item to add to the cart or type 'end' to stop adding items: ").strip().lower()
        
        if user_input == 'end':
            break
        
        if user_input in items:
            cart.append(user_input)
        else:
            print(f"'{user_input}' is not in stock.")
    
    return cart

def calc_total(cart, prices):
    subtotal = 0
    
    print("\nGrocery Checkout Receipt")
    
    item_width = 10
    price_width = 10
    sub_width = 5

    print('-' * (item_width + price_width))
    
    for item in cart:
        price = prices.get(item, 0)
        subtotal += price
        print(f"{item:<{item_width}}${price:>{price_width}.2f}")
    
    tax_rate = 0.02
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(" ")
    print(f"{'Subtotal:':<{item_width}}${subtotal:>{sub_width}.2f}")
    print(" ")
    print(f"{'Tax:':<{item_width}}${tax:>{price_width}.2f}")
    print(f"{'Total:':<{item_width}}${total:>{price_width}.2f}")
    
    return total

def calculate_change(total, cash_given):
    change = cash_given - total
    
    if change < 0:
        print("Insufficient cash provided.")
        return
    
    dollars = int(change)
    cents = int(round((change - dollars) * 100))
    
    quarters = cents // 25
    cents %= 25
    cents %= 10
    pennies = cents % 5
    
    print(f"\nThe change owed to you is ${change:.2f}")
    print(" ")
    print(f"Dispensing...")
    print(" ")
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{pennies} Pennies")

def main():
    prices = {
        'apples': 3.69,
        'berries': 4.00,
        'chocolate': 2.89,
        'cheese': 4.00,
        'pepsi': 7.89,
        'turkey': 6.99,
        'eggs': 3.50,
        'bread': 3.00
    }
    
    show_avail_items(prices)
    
    cart = add_items_to_cart(prices)
    
    print("\nThe items currently in your cart are:")
    for item in cart:
        print(f"- {item}")
    
    total_cost = calc_total(cart, prices)
    
    print(f"\nYou owe: ${total_cost:.2f} for the groceries")
    
    cash_given = float(input("\nHow much cash will you put in the self-checkout machine: $"))
    
    calculate_change(total_cost, cash_given)

if __name__ == "__main__":
    main()
