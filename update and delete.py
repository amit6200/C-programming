#update
l=[10,20,30,40,50]
l[2]=300
print(l)

#pop
#remove
#clear
#del

r=l.pop(0)
print(l,r)

l.remove(20)
print(l)

l.clear()
print(l)

#del l
#print(l)

l=[50,40,30,20,10]
print(l.sort())
print(l)
l.reverse()
print(l)


l3=sorted(l)
print(l3) 


print(l.index(30))

print(l.count(30))


l=[10,20,30,40]
l2=[100,200,300]
print(l+l2)

l=[0.1]
print(l*10)