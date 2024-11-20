# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import random
x = random.randint(1,101)
y = random.randint(1,101)
print ("What is the sum of these two numbers?",   x, "+", y) 
z = x + y
a = int(input())

for i in range (int(a)):
    if str(z)== i:
        print ("y")
        break