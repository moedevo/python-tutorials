#Program to test whether a number is within 100 of 1000 or 2000

n = int(input('Enter Number:'))
if  n in range(100,1000):
  print(True)
  print('Number withen 100 of 1000')
elif n in range(1000,2000):
  print(True)
  print('Number withen 100 of 2000')
elif n > 2000:
  print(False)
  print('Number is greater than 2000')
elif n < 100:
  print(False)
  print('Number is less than 100')