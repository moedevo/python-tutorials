#Get the difference between a given number and 17
#if the number is greater than 17 return double the absolute difference.

n =int(input("Enter Number :"))

if n > 17 :
  a = 17 - n
  a = abs (a) *2
  print(a)

else :
  a = (17-n)
  print(a)