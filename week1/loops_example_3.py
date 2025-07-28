'''You are building an ATM-style PIN entry system.

The correct PIN is 4321.

The user has 3 chances to enter the correct PIN.

If they get it right, print: "Access granted!" and stop.

If they fail all 3 attempts, print: "Card blocked. Too many wrong attempts."'''

for i in range(3,0,-1):
    pin = int(input("enter your 4 digit "))
    if pin == 4321:
        print("access granted")
        break
    else:
        if i > 1:
            print(f"try again , you have {i -1} attempt left")

    
        else:

            print("too many attempts, acrd access denied")
        
        