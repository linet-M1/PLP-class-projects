# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Ask user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print("Discount applied!")
    print("The final price is:", final_price)
else:
    print("No discount applied.")
    print("The price remains:", final_price)