#tuple
t=(10,20,30,40)
print(t,type(t))
#immutable datastructure
#ordered indexing and slicing
print(t[-1])

print(t[:3])

print(t.index(20))

l=[10,20,30,40,50]
for t in enumerate(l):
    print(t)
l=[10,20,30,40,50]
t=tuple(l)
print(t)

t=("a","b","c",100)
l=list(t)
print(l)