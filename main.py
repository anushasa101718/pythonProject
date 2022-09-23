empinfo = {'name':'anusha', 'id':100662607, 'sal': '1l$'}
print(empinfo)
print(empinfo['id'])

# printing keys of the dictionaries

for i in empinfo:
    print(i)

# printing both keys and values

for i in empinfo:
    print(i,empinfo[i])

# using inbuilt function to print keys

for key in empinfo.keys():
    print(key)

# inbuilt function to print values

for val in empinfo.values():
    print(val)

# printing both keys and values

for key,val in empinfo.items():
    print(key,val)

# removing items from dictionaries

empinfo.pop('name')
print(empinfo)

empinfo.pop('id')
print(empinfo)

#del empinfo[id]
#print(empinfo)

empinfo.clear()
print(empinfo)