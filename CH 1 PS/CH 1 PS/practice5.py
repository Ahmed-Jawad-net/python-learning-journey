#Shopping Bill
price1 = float(input("Enter the price of first item: "))
quantity1 = int(input("Enter the quantity of first item: "))
price2 = float(input("Enter the price of second item: "))
quantity2 = int(input("Enter the quantity of second item: "))

total_price = (price1 * quantity1) + (price2 * quantity2)
print(f"Your total bill is: {total_price:.2f}") #:.2f formats the total price to 2 decimal places
