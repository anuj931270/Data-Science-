# Tax Calculation for Car Purchase
brand = input("Enter car brand (Mahindra, Audi, Jaguar, Mercedes): ").strip().capitalize()
price = float(input("Enter car price in Lakhs (e.g., 12.5): "))

tax = 0
valid_input = True

# 2. Check the brand and price to calculate tax
if brand == "Mahindra" and 7 <= price <= 10:
    tax = price * 0.05  # 5% tax

elif brand == "Audi" and 10 <= price <= 15:
    tax = price * 0.10  # 10% tax

elif brand == "Jaguar" and 15 <= price <= 20:
    tax = price * 0.25  # 25% tax

elif brand == "Mercedes" and 20 <= price <= 25:
    tax = price * 0.30  # 30% tax

else:
    print("Error: Either the brand name is incorrect or the price is outside the tax bracket.")
    valid_input = False

# 3. Print the output if everything is valid
if valid_input:
    print(f"Calculated Tax: {tax:.2f} Lakh")
    print(f"Total Price (with tax): {price + tax:.2f} Lakh")