#Write a program that prints numbers from 1 to 30.
#But for every number divisible by 3, instead of the number, print "Clap!"

for i in range(1,31):
    if i % 3 == 0:
        print("Clap")
    else:
        print(i)

