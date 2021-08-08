#Program to to calculate the sum of three given numbers,
#if the values are equal then return three times of their sum.

n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))
n3 = int(input('Enter Third Number: '))

sum = n1 + n2 + n3

if n1 == n2 == n3 :
  print(sum * 3)
  
else :
  print(sum)
  
#AnotherSolution

def cal(x,y,z):
  sum = x + y + z
  if x == y == z :
    sum = sum * 3
    return sum
print(cal(2,2,2))



