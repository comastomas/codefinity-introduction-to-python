grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30),
"Bread": ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50)}
egg_category, egg_price, egg_stock = grocery_inventory['Eggs']
if egg_price > 5: print("Eggs are too expensive, reducing the price by $1.") 
if egg_price > 5: egg_price = egg_price - 1
else: print("The price of Eggs is reasonable.")
grocery_inventory["Eggs"] = egg_category, egg_price, egg_stock
grocery_inventory["Tomatoes"]=("Produce", 1.20, 30)
print("inventory after adding Tomatoes:",grocery_inventory)
milk_cat, milk_price, milk_inventory = grocery_inventory["Milk"]
if milk_inventory < 10: 
    print("Milk needs to be restocked. Increasing stock by 20 units.")
if milk_inventory < 10: milk_inventory = milk_inventory + 20
grocery_inventory["Milk"] = milk_cat, milk_price, milk_inventory
if milk_inventory >= 10: print("Milk has sufficient stock.")
apple_price = grocery_inventory["Apples"][1]
if apple_price > 2: 
    grocery_inventory.pop("apples") 
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)