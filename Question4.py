#Marissa Jones
#11-7-2023

#Lab Activity Module 7

def removeDup(list):
    res = []  # new empty list

    for i in list:  #each element in the list
        if i not in res:
            res.append(i)

    print("After removing duplicates, list = ", res)


list = [1, 3, 3, 3, 6, 2, 3, 5]  # original list
removeDup(list)