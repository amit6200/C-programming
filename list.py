#list
#1lists are mutable-add update and delete
#2ordered indexing and slicing
#3heterogeneous datatype
l=[10,20,30,40,"python","java",[100,200,300]]
print(l,type(l))

#indexing and slicing 
print(l[-1][1])
 
print(l[1:3])

l=[100,200,300,400,500]
for value in l:
   print(value)
for value in l[::2]:
    print(value)
#append
print(id(l))
l.append(600)
print(l)
print(id(l))
#extend
l.extend([500,600,700,800])
print(l) 
l.append([500,600,700,800])
print(l)
#insert
l.insert(0,1000)
print(l)
l=[10,20,30]
l2=l
print(l,l2)
print(id(l))
print(id(l2))




