#Marissa Jones
#10-10-2023

#

starting_day = int(input("Enter the starting day number (0-6, where 0 is Sunday and 6 is Saturday): "))
stay_length = int(input("Enter the length of your stay: "))

return_day = ((starting_day + stay_length) % 7) - 1

print("You will return on day number", return_day, "which is:", ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][return_day])