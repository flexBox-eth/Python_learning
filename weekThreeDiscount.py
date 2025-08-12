def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Print result
if final_price < original_price:
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {original_price:.2f}")
