#a list function of multiplication table
n= int(input("Type your number: "))
table = [n*i for i in range(1, 11)]
for num in table:
   print(num)

print("Final Table is ",table)