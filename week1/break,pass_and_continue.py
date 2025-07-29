#Write a Python program that:

#Takes a list of 10 integers (can be positive, negative, or zero).

#Loops through the list.

#Ignores (pass) all zeros.

##Skips (continue) any negative numbers.

#Breaks the loop if a number greater than 100 is found.

#Adds up all the remaining positive numbers (≤100) and prints the sum.
nums = []

for i in range(10):
    number = int(input("enter 10 numbers: "))
    nums.append(number)

total = 0    


for number in nums:
    if number == 0:
        pass
    elif number < 0:
        continue
    elif number > 100:
        break
    else: 
        total += number

print("the sum of the numbers is",total)


