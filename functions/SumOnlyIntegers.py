#Write a Python program to add two objects if both objects are an integer type

def addition(x,y):
    if not isinstance(x,int) and isinstance(y,int):
        raise TypeError("Inputs must be integers!")
    return x + y 
print(addition("hell",5))