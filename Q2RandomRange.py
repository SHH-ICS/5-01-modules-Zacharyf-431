# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.


import random
x = input ("Enter value A:   ")
y = input ("Enter value B:   ")
if float(x) > float(y):
    print ("The value of B must be greater than the value of A")
else:
    print (random.randint(int(x),int(y)))