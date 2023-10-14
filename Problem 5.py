#Marissa Jones
#10-10-2023

# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.

miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

print(f"Your car's MPG is: {mpg:.2f} miles per gallon")