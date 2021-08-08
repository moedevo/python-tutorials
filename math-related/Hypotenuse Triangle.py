#Write a Python program to calculate the hypotenuse of a right angled triangle
import math

def hypotenuse(a,b):
    hypotenuse = math.sqrt((a**2) + (b**2))
    return hypotenuse
print(hypotenuse(3,4))