#A program to accept a filename from the user and print the extension of that.

file_name = input('Enter your filename :')
file_extension = file_name.split('.')
print('You file extension is : ', repr(file_extension[-1]))
