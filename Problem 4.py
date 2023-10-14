#Marissa Jones
#10-10-2023

#Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

from math import pi
r= float(input("Enter radius of circle:"))
area= pi*r*r
print("Area of the circle is: ","{:.3f}".format(area))