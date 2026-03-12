# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for items, details in inventory.items():
    if details[0] < 30:
        print(f"{items} need restocking.")
    if details[0] > 100:
        print(f"{items} should be sold at the discounted price of {details[2]}.")
    if details[0] >= 30 <= 100:
        print(f"{items} should be sold at the regular price of {details[1]}.")
    
    