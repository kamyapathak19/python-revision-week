operator = input("enter your operator +,-,*,/")
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))


match operator:

    case  '+' :
        print(f"the addition is {num1 + num2}")

    case '-':
        print(f"the subtraction is {num1-num2}")

    case '*':
        print(f"the product is {num1*num2}")

    case '/':
        if num2 == 0:

           print("num2 cant be 0")

        else:   

            print(f"the quotient is {num1/num2}")


    case  _:
        
        print("pls enter valid input")



