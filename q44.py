#read a text file and write no of lines
with open("q43Log.txt") as l:
    content = l.readlines()

lineno= 1
for line in content:
    if("python" in line):
        print(f"Yes the word python is in the file. Line no:{lineno}")
        break
    lineno += 1
    
else:
    print("Sorry the word python is not in the file")
    