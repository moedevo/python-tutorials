#Write a Python program to convert the distance (in feet) to inches, yards, and miles

distance_feet = float(input("Input Distance in Feet: "))

distance_inches = distance_feet * 12
print("Distance in Inch: ", distance_inches)

distance_yards = distance_feet / 3
print("Distance in Yards: ", distance_yards)

distance_miles = distance_feet /5280
print("Distance in Miles: ", distance_miles)