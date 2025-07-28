'''You're helping a mini grocery store app. A customer adds items to their cart one by one, and your program should:

Ask the user for each item price.

Keep adding prices to a list.

Stop when the user types "done".

Print the total number of items, the list of prices, and the total amount to pay.'''

cart = []

while True:

    stuff = input("enter price of the item(or press done when you are done)")
    if stuff == "done":
        break
    else:
        try:
            price = float(stuff)
        
            cart.append(price)

        except ValueError:
            print("enter valid input")    
        
        

print(f"total number of items are:{len(cart)}")
print("prices:", cart)
print("total sum", sum(cart))