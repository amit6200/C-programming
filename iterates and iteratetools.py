


import itertools
from re import I


l=[1000,200,300,400,500]
i=iter(l)


#print(next(i))
#print(next(i))

for value in i:
 print(value)
 
 
 l=[1,2,3,4,5]
 l1=[10,20,30,40,50]
 l2=[34,45,67,12,13]
 
 i=itertools.chain(l,l1,l2)
 
 for value in i:
     print(value)
 