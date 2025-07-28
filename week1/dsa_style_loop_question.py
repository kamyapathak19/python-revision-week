#Write a program that takes a number as input (e.g., 1223451) and prints how many digits in it are unique (i.e., appear only once).
num = input ("enter a number: ")# we will take a string 
count = {}

for digit in num:
    if digit in count:
        count[digit] +=1
    else:
        count[digit] = 1

print("digital frequency")
for key,  value in count.items():
    print(f"the {key} appears {value} time(s)")

    

