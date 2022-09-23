def SumOfNum():
    num1 = 2
    num2 = 3
    sum = num1+num2

    print(sum)
SumOfNum()

### if we wanna use return

def SumOfNum():
    num1 = 2
    num2 = 3
    sum = num1+num2
    return sum
print(SumOfNum())

### function with passing arguments

def wish(name):
    print("hello {}".format(name))

wish("Anu")
wish("Krish")