from ast import arguments, keyword
from tkinter import Variable
#Variable arguments
#l=[100,200,300,400]
#l.append(500,250,350)
#print(l)


def add_value(*args):
    l=[]
    for value in args:
        l.append(value)
    return l
 
    
result=add_value(100,200,300,400,500)
print(result)
result=add_value(100,200)
print(result)
result=add_value(100,200,300,400,500,600,700,800)
print(result)


#Variable keyword arguments
def get_details(**kwargs):
    print(kwargs)
get_details(name="amit",email="amit@gmail.com",contact=3000956444,dob="24-08-2003")
            