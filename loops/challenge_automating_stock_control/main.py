# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for current_stock, details in inventory.items():
    print(f"Processing", current_stock)
    while details[0] < details [1]:
        details[0] += details[2]
        if details[0] > discount_threshold:
            details[3] = True
    print(current_stock, details)
print("Processing completed")        