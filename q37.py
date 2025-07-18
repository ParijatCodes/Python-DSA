#a function to remove and strip a particular word from a list
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.replace(word, ""))
    return n
l= ["harry", "Rohan", "Sujan", "an", "Subham", "gangi"]
print(rem(l, "an"))