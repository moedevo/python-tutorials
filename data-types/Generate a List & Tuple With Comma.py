#Generate a list and tuple with comma-separated numbers

values = input('Enter Numbers seperaed by commas : ')
list = values.split(',')
tuple = tuple(list)
print('List :',list)
print('Tuple:', tuple)

