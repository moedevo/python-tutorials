def con(items): #We Define The Function
    result = " " #Empty the result at first
    for n in items:
        result += str(n) # It takes one item and returning as a value then the other until the list is finished
    return result
print(con([1,2,3,4,5]))