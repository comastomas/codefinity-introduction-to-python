seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = True if seasonal and current_stock > high_stock_threshold else False
discount_eligible = True if not selling_well and not on_sale else False
make_discount = True if overstock_risk or discount_eligible else False

print("Should the item be discounted?", make_discount)