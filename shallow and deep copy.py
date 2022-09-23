# = operator

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

#So, if you want to modify any values in new_list or old_list, the change is visible in both.
#As you can see from the output both variables old_list and new_list shares the same id.

##############################################################################################################################
# Shallow copy : A shallow copy creates a new object which stores the reference of the original elements.

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

# This means it will create new and independent object with same content. To verify this, we print the both old_list and new_list but check below

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

#In the above program, we created a shallow copy of old_list. The new_list contains references to original nested objects stored in old_list.
#Then we add the new list i.e [4, 4, 4] into old_list. This new sublist was not copied in new_list.

#However, when you change any nested objects in old_list, the changes appear in new_list. check below code

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

#####################################################################################################################

# Deep copy: A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

#However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)