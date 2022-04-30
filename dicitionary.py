#dict
#1 mutable
#2 unordered
#3 key should be unique
#4 keys should immutable
d={"emp_id":101,"name":"ABC","email":"abc@gmail.com"}
print(d)
#update dicitionary
d["contact_no"]=12339000000
print(d)

#get
#setdefault

print(d.get("emp_id"))
print(d.setdefault("emp_id"))

for x in d:
    print(x) 
for key in d:
    print(key,d[key])
    
    
d={}
for value in range(1,11):
    d[value]=value*value
    print(d)
#keys
#values
#items
d={"emp_id":101,"name":"ABC","email":"abc@gmail.com"}
print(d.keys())
print(d.values())
print(d.items())