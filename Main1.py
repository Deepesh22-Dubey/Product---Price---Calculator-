print("Welcome to Product Price Calculator! ")
# Product Price Calculator
original_price = float(input("Enter Original Price: "))
discount_percent = float(input("Enter Discount %: "))
discount_amount = discount_percent / 100 * original_price
final_price = original_price - discount_amount

print(" Thank you for using Product Price Calculator!")
print("Hope you enjoyed that!")
