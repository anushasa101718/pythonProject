studentDtls = ['name','id', 'loc']
studentInfo = ['xyz',8,'chicago']
#convert these lists into dict

res = {}
for key in studentDtls:
    for value in studentInfo:
         res[key] = value
         studentInfo.remove(value)
         break
print(res)

# list comprehensions
# Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
#Advantages of List Comprehension
#More time-efficient and space-efficient than loops.
#Require fewer lines of code.
#Transforms iterative statement into a formula.

# dict compreshensions

# what is the difference between pass and continue
# what is the difference between deep copy and shallow copy

### what is the difference between xrange vs range**************