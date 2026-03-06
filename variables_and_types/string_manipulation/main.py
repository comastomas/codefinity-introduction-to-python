grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = grocery_items [0:4]
dairy2 = grocery_items [6:11]
bakery1 = grocery_items [13:17]
aisle5 = dairy1 + ' ' + dairy2 + ' ' + bakery1

print(f'We have dairy and bakery items: {dairy1}, {dairy2} and {bakery1} in aisle 5')