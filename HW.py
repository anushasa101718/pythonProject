dictTest = {'name':'anusha', 'id':100662607, 'sal': '1l$'}
dict1 = []
#dict1.append(dictTest.keys())
#print(dictTest.keys())
#print(dict1)

dict2 = []
#dict2.append(dictTest.values())
#print(dict2)

for key, val in dictTest.items():
    dict1.append(key)
    dict2.append(val)
print(dict1,dict2)

