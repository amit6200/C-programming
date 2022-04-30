


#factorial(5) = 5 * fact(4)
#                        4 * fact(3)
#                             3 * fact(2)
#                                   2 * fact(1)
#                                            1

from math import factorial
from unittest import result

def factorial (num):
    if num==1:
        return 1
    else:
        return num *factorial(num-1)

num1=5
result=factorial(num1)
print(result)



def binary_search(l,key):
    
    if len (l)==0:
        return False
    else:
        mid=len(l)//2
    
    if l[mid]==key:
        return True
    elif key<l[mid]:
        return binary_search(l[:mid],key)
    else:
        return binary_search(l[mid+1:],key)
    



l=[100,200,300,400,500,600,700,800,900]
key=10

result=binary_search(l,key)
print(result)






