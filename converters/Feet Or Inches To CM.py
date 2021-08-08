height = input("Choose Feet or Inch: ")

if height == "Feet" or height == "feet":
    height_feet = float(input("Enter Height in Feet: "))
    height_cm = height_feet * 30.48
    print("Height in Centimeter: ",height_cm)

elif height == "Inch" or height == "inch":
    height_inch = float(input("Enter Height in Inches: "))
    height_cm = height_inch * 2.54
    print("Height in Centimeter",height_cm)

else:
    print("Error! Check Your Spelling Carefully!")