#Write a program that lets the user build their own pizza by adding toppings one by one.

#Ask: "Enter a topping (or type 'done' to finish):"

#Keep accepting toppings until the user types "done"

#After that, print the full list of toppings they added.


toppings = []
while True:
    topping = input("enter a topping (or type done to finish)")
    if topping == "done":
        break 
    toppings.append(topping)

    print("your pizza will have:",",".join(toppings))


