#a program to check if contents in two files are same
with open("q45This.txt") as t:
    content= t.read()
with open("q45That.txt") as t1:
    content1= t1.read()
    
if (content == content1):
    print("Both the files have same content")
else:
    print("The contents are different")