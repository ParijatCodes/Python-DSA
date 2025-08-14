#print specific elements(3rd, 5th, 7th) from a list using enumerate 
l= [1,2,3,4,6,8,9]
for i,item in enumerate(l):
    if i==2 or i==4 or i==6:
        print(f"The element at {i} is {item}\n  ")
        i+=1