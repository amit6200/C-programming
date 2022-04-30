#help(str)
#print(dir(str)) 
#format
num1=100
num2=200
print("value of num1 is",num1,"value of num2",num2)
print("value of num1 is {} value of num2 {}".format(num1,num2))


s="python sample string"
print(id(s))
s=s.capitalize()
print(s)
print(id(s))
#upper
#lower
#title

print(s.upper())
print(s.lower())
print(s.title())

#isupper
#islower
#istitle
#iscapitalize

#split
#join


s="HTML,CSS,PYTHON,JAVA,Django"
l=s.split(", ")
print(l)

sl=(" ").join(l)
print(sl)



s1="abcd"
s2="1234"

s3="python sample string abcd"

table=str.maketrans(s1,s2)
result=s3.translate(table)
print(result)
#maketrans
#translate


#index
#find
#rfind function

s="HTML,CSS,PYTHON,PYTHON,PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))
print(s.find("python"))
print(s.rfind("PYTHON"))


s="******this is sample string****"
s1=s.strip("*")
print(s1)


s="python"
s1=s.center(20,"*")
print(s1)
s1=s.ljust(20,"*")
print(s1)
s1=s.rjust(20,"*")
print(s1)



s="html,css,python,html"
s1=s.replace("html","HTML5")
print(s1)