list1 = [56, 52, 5, 6, 3, 2, 1, 4, 54, 1, 151, 54, 23, 7, 89, 55, 54, 54, 14, 1]

while len(list1) > 1:
    l = len(list1)
    for i in range(l - 1):
        if list1[i] > list1[i + 1]:
            list1.pop(i + 1)
        else:
            list1.pop(i)
        break

print("Greatest number is:", list1[0])    
    


