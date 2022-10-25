# Inputs 
Name = input("Enter your name:")
print("Hello, " + Name) 

OrginalPrice = eval(input("Enter the orginal sale price of the item:"))

Discount =  eval(input("Enter the discount percentage that you have been given:"))

# Sales Price Calculated 
DiscountedPrice = OrginalPrice - (OrginalPrice * Discount/100)

#OutPut
print("The cost of the item will be $ ", + round(DiscountedPrice))
