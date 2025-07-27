#rename a file without using any library
text= input("Write file name: ")
with open(text) as t:
    content= t.read()
with open("q48rename_by_python.txt","w") as t2:
    t2.write(content)