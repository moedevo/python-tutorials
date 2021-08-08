# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
 
def sum(x,y):
    if x == y :
         return True
    elif x + y == 5 :
        return True
    elif abs(x - y) == 5 :
        return True
    else:
        return False
print(sum(-5,10))