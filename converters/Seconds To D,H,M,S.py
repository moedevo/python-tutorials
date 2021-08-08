#Write a Python program to convert seconds to day, hour, minutes and seconds

time = float(input("Input time in seconds: "))

day = time // (86400)
time = time % (86400)

hour = time // 3600
time = time % 3600

minutes = time // 60
time = time % 60

seconds = time

print(f''' 
D: {day}
H: {hour} 
M: {minutes} 
S: {seconds}''')