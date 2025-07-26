#SEARCH FOR A PARTICULAR WORD IN A TEXT FILE
q = open("q39_poem.txt")
inside=q.read()
n_inside= inside.lower()
if("twinkle" in n_inside):
    print("The word twinkle is present in the file")
else:
    print("The word twinkle is not present in the file")

q.close()