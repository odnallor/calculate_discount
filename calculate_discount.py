def calculate_discount(price, discount_percent):
    if discount_percent >= 20: #checking if the discount percent is greater than 20
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompting user for inputs
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating and printing the final price
final_price = calculate_discount(original_price, discount_percentage)
if final_price != original_price:
    print("Final price after applying the discount:", final_price)
else:
    print("No discount applied, final price remains the same:", original_price)
