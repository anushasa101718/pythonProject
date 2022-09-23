def func1():
    '''this is my first function'''

print(func1.__doc__) # __doc__ is called magic methods or dunder methods

#######################################################
def func1():
    return "Hello"

print(func1())
print(func1)

######################################################

def display():
    name = 'xyz'
    print(name)
display()