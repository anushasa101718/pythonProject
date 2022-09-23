## Sum of 1st 10 numbers

sum = 0
for i in range(1,11):
    sum = sum + i
    print(sum)


sum = 0
x = int(input("Enter the min value:"))
y = int(input("Enter the max value:"))
for i in range(x,y):
    sum = sum + i

print(sum)