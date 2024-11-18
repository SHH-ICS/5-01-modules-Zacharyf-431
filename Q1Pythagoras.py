# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.

import math
x = input ("Enter length of side A:     " )
y = input ("Enter length of side B:     " )

if x == "0":
    print ("Your input must be a valid integer")
elif y == "0":
    print ("Your input must be a valid integer")
else:
    a = float(x) ** 2
    b = float(y) ** 2
    c = float(a) + float(b)
    print ("Side C is equal to:        ", math.sqrt(float(c)))
