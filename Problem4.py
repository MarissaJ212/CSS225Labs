#Marissa Jones
#11-14-2023

#CSS225 Lab Activity Week 8

def checkLeapYear(year):

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))

        else:
            print("{0} is not a leap year".format(year))

    else:
        print("{0} is a leap year".format(year))

checkLeapYear(2021)
checkLeapYear(2000)