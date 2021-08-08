#Program to calculate number of days between two dates.

import datetime

#first date
year1 = (int(input('Enter the year of the first date: ')))
month1 = (int(input('Enter the month of the first date: ')))
day1 = int(input('Enter the day of the first date:'))
#second date
year2 = int(input('Enter the year of the second date: '))
month2 = int(input('Enter the month of the second date: '))
day2 = int(input('Enter the day of the second date: '))

x = datetime.datetime(year1,month1,day1)
y = datetime.datetime(year2,month2,day2)

delta = abs(x-y)
print(f'The Number Of Days between {x} and {y} is : {delta.days} '.format(x,y,delta.days))
