list1 = [1,2,3,1,2,3,1,2,1,2]
list2 = []

for num in list1:
    if num not in list2:
        list2.append(num)
    else:
        list1.remove(num)
print(list2)
print(list1)

# with set function
list1 = list(set(list1))
print(list1)