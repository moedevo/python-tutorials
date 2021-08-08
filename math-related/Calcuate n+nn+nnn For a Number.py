#A program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input('Enter the value of n: '))
 
x = n * 1
y = n * 11
z = n * 111

print('the value of n+nn+nnn: ',x+y+z)