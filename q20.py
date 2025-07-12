#spam message checker
s1= "Make a lot of money"
s2= "buy now"
s3= "subscribe this"
s4="click this"

text=input("Enter your message:\t")
#checking
if((s1 in text) or (s2 in text) or (s3 in text) or (s4 in text) ):
    print("This is a spam message")
else:
    print("This message is safe")