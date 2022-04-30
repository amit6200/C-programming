 #positional argument
 
def linear_search(l,key):
    for value in l:
      if key==value:
          return True
      else:
          return False

l=[100,200,300,400,500]
key=4000
result= linear_search(l,key) 
print(result)
#default argument
#8 char
#1upper
#1lower
#1special char
#digits


print(ord('a'),ord('z'))

from ast import keyword
from audioop import add
import random
from tkinter import Variable
def gen_passwprd():
    l=['@','#','$','&']
    
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digit=random.randint(10000,99999)
    password=upper+lower+special+str(digit)
    return password
    
result=gen_passwprd()
print(result)

#keyword


def validate(username,password):
    if username=="ABC" and password=="Abc@123":
        print("valid password")
    else:
        print("invalid password")
        
        
validate("abc123","Abc@123")   



 
def add_value(*args):
   print(args)
   


add_value(100,200,300,400,500)

add_value(100,200)

add_value(100,200,300,400,500,600,700,800)

#Variable length keyword args

# name,email,contact,dob
def get_details(**kwargs):
    print(kwargs)

get_details(name="ABC",email="amitsingh.1covid19@gmail.com",contact=8318656200,dob="24-08-2003")


