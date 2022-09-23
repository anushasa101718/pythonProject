list1 = [2,3,5,6,8,9,11,13]
even = []
odd = []

for x in list1:
    if x%2 == 0 :
        even.append(x)
    else:
        odd.append(x)
print(even,odd)
