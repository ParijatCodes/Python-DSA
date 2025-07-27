#find a particular word in a file
with open("q43Log.txt") as l:
    content= l.read()
if ("python" in content):
    print("Yes the word python is in the file")
else:
    print("Sorry the word python is not in the file")