#Marissa Jones
# 10-24-23
# If, else/elif statements

for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(str(i)+" is Divisible by three and five")
    elif(i%5==0):
        print(str(i)+" is Divisible by five")
    elif(i%3==0):
        print(str(i)+" is Divisible by three")
    else:
        print("",end="")