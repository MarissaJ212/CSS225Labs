#Marissa Jones
#11-7-2023

#Lab Activity Module 7

import math

def area_of_circle(r):

    if not isinstance(r, (float, int)):
        raise ValueError("Radius should be a floating point or integer datatype.")

    if r < 0:
        raise ValueError("Radius can't be negative.")

    area = math.pi * r ** 2
    return area

radius = 5.0
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")

