'''
You are building a system to analyze student performance. Write a Python program that:

Takes a student's score (0 to 100) as input.

Assigns a grade using the following rules:

90 and above → A

80 to 89 → B

70 to 79 → C

60 to 69 → D

Below 60 → F

If the student gets a C but their score is divisible by 5, they get a bonus grade bump to B.

If the student gets a D and their score ends with a 7, they also get a bump to C.

If the student scores exactly 100, print: "Perfect score! A+" and skip other rules.

'''

count = 0

while count < 60:
    

   marks = int(input("enter your marks out of humdred: "))

   if marks < 0 or marks > 100:
    print("invalid marks pls enter the correct marks: ")


   elif marks == 100:
    print("Perfect score! A+")

   elif marks >= 90:
    print("congrats you have scored A grade")

   elif marks >= 80:
    print("keep it up you have scored B grade")

   elif marks >= 70:
    if marks % 5 == 0:
        print("bonus you are bumped to B grade")
    else:    
        print("keep it up you have scored C grade")

   elif marks >= 60:
    if marks % 10 == 7:
        print("congrats you are bumped to C grade")
    else:    
        print("you need to work a lil more hard and you have scored D grade")

   else:
    print("sorry but you are failed work harder next time")

count+= 1
