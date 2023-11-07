#Marissa Jones
#11-7-2023

#Lab Activity Module 7

def check(var):
    if var in range(1,10): # will return true if it's in range
        print("It is in range")
    else:
        print("Not in range")

var = int(input("Enter a number "))
check(var)