import string


name="amit is smart"
d=name[-1]
#print(d)
letter='''Dear <|NAME|>
hello congrulation you are select in google as a software engineer
you are selected!
Date:<|DATE|>
'''
name=input("enter the name\n")
date=input("enter date\n")
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
#print(letter)
st="Ram is go to school"

doublespaces=st.find("  ")
#print(doublespaces)