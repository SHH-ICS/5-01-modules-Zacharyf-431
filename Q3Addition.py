# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random
x = random.randint(1,101)
y = random.randint(1,101)
print ("What is the sum of these two numbers?",   x, "+", y) 
try:
    z = x + y
    a = int(input())
    if a == int(z):
        print ("That is correct. You get a Cookie!!!!")
    else:
        print ("You are incorrect. No Coookie for you!!!!")
except ValueError:
    print ("Put in a valid number")
