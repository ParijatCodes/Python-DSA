#replace a word in a file with "####"
words = ["donkey","gadha", "hati"]

with open("q42Textfile.txt", "r") as f:
    content= f.read()
for word in words:
    content= content.replace(word, "#"*len(word))

with open("q42Textfile.txt", "w") as w:
    w.write(content)
