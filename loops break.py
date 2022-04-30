l=[10,20,30,40,50,60]
key=400
for value in l:
    if value == key:
        print("Element found")
        break
    else:
        continue
else: 
        print("Element not found")
for index,value in enumerate(l):
    print (index,value)