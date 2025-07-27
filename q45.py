#copy a file's text and print it
with open("q45This.txt") as t:
    content= t.read()
with open("q45That.txt","w") as t2:
    t2.write(content)