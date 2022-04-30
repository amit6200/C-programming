#string :
#s=' '  "" """ """
#1 string are immutable
#2 string is ordered data structure -indexing and slicing


# s="python sample string"
# print(type(s))

s1="python"
print(id(s1))

#indexing

s="python sample string"
print(s[0])

#slicing

print(s[0:])
print(s[0:6])
print(s[:6])
print(s[7:])

#stride
print(s[::3])

for value in s:
    print(value)
    
help(str)
    
