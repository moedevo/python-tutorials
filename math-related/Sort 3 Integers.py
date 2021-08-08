def sort(x,y,z):
    a1 = min(x,y,z)
    a3 = max(x,y,z)
    a2 = (x+y+z)-a1-a3
    return a1 , a2 , a3
print(sort(5,2,7))