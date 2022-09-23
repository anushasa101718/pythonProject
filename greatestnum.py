x = input('Enter 1st number')
y = input('Enter 2nd number')
z = input('Enter 3rd number')

if x > y and x > z:
    print('1 st number is greatest',x)
elif y > x and y > z :
    print('2nd number is greatest',y)
else:
    print('3nd number is greatest',z)