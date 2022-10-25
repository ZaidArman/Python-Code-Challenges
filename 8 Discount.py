####  8 Discount in the product #######

# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.


# Code Here

def Discount(FullPrice, Discount_Perc):
    
    DiscountApplied = 0
    Discount = (Discount_Perc/100)*Full_Price
    DiscountApplied = Full_Price - Discount
    return DiscountApplied

Full_Price = int(input("Enter full price of the product:... "))
Discount_Percentage = int(input("Enter Discount Percentage of the product:... "))

print(Discount(Full_Price, Discount_Percentage))