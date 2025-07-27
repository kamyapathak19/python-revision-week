'''You're writing a Python program for a small fast-food counter. Based on what the user types in, your program should calculate the price.

Here’s the menu:

nginx
Copy
Edit
Burger - ₹120
Fries - ₹60
Pizza - ₹250
Sandwich - ₹80
✅ Your task:
Ask the user what they want to order using input().

Based on their order, print:

"You ordered <item>. That will be ₹<price>."

If they type something not on the menu, print:

"Sorry, we don't have that item."'''

count = 1

while count < 100:
    print(" menu for today\n burger = $120\n fries = $60\n pizza = $250\n sandwhich = $80 ")

    menu = {"burger":120, "fries":60, "pizza":250, "sandwhich":80}
    food = input("what is your order for today, pls stick to one thing:").lower()
    if food in menu:
        print(f"so your food is {food} and your total is ${menu[food]}")

    else:
        print("pls order from the menu")

    count+=1        
