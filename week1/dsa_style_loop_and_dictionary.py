#Given a string, write a Python program to find the character that appears most frequently in the string (excluding spaces). If there are multiple characters with the same highest frequency, return any one of them.
boli = input("enter your word: ")

word = {}

for char in boli:
    if char in word:
        word[char]+= 1
    else:
        word[char]= 1

max_frequency = 0
max_char = ''

for char in word:
    if word[char]> max_frequency:
        max_frequency = word[char]
        max_char = char 
        
print(f"the word with maximum frequency is {max_char}, and its repeated {max_frequency} times")
