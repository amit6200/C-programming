#map
#filter
#lambda

from operator import truediv


def sqr(num1):
    return num1**2


l=[10,20,30,40,50]
result=list(map(sqr,l))
print(result)
for value in result:
 
 
 def add(num1,num2):
     return num1+num2
  
 l1=[100,200,300]
 l2=[10,20,30]
 
 result=list(map(add,l1,l2))
 print(result)
 
 
 
 def check_num(num1):
     if num1 %2==0:
         return True
     else:
         return False
 
 
 
 
 l=[100,125,200,545,300]
 
 result=list(filter(check_num,l))
 print(result)
 
 
 
#lambda
l=[10,20,30,40]
result=list(map(lambda num1:num1**2,l))
print(result)

d={1:20,3:30,2:50}

l=sorted(d.items())
print(l)