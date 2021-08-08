#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

Fnumber = int(input("Enter First Number: "))
Snumber = int(input("Enter Second Number: "))
Tnumber = int(input("Enter Third Number: "))



if Fnumber == Snumber or Fnumber == Tnumber or Snumber == Tnumber:
   print(0)
else:
    sum = Fnumber + Snumber + Tnumber
    print(sum)

#OR

def sum(x,y,z):
    if x == y or x == z or y == z:
        return 0
    else:
        sum = x + y + z
        return sum
print(sum(1,1,2))
        