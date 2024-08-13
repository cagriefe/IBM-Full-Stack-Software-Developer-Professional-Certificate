import numpy as np

def welcome():
    message = "Welcome to the course!"
    return print(message)

def add(a,b):
    a = np.array(a)
    b = np.array(b)
    if (a[0]+b[0]) <= 5:
        return print("The sum of the first elements is less or equal to 5")
    else:
        return print(a+b)
    
def abstract(a,b):
    a = np.array(a)
    b = np.array(b)
    if (a[0] - b[0]) <= 5:
        return print("The difference of the first elements is less or equal to 5")
    else:
        return print(a-b)
    
welcome()

add([1,2,3],[4,5,6])
add([1,2,3],[5,5,6])

abstract([5,2,3],[4,5,6])
abstract([15,2,3],[4,5,6])
