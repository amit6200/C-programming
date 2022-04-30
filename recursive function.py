
from math import factorial
from unittest import result

def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)
num1=5
result=factorial(num1)
print(result)