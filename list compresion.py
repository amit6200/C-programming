l=[100,200,300,400,500]
l2=[]

for value in l:
    l2.append(value*value)
print(l2)


l=[100,200,300,400,500]
l2=[value*value for value in l]
print(l2)



l=[100,250,500,600,10,2030,30,35,3,9]
l2=[value for value in l if value%2==0]
l3=[value for value in l if value%2!=0]
print(l2)
print(l3)


l5=['abc','abcd','zzzz']
l4=[len(value) for value in l5]
print(l4)

l=[100,105,304,507]
l2=["even"if value%2==0 else "odd" for value in l]
print(l2)

a={r:r**2 for r in range(1,12)}
print(a)
