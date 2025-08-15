#store multiplication table in txt file
n= int(input("Type your number: "))
table = [n*i for i in range(1, 11)]
with open("MultiTables.txt", "a") as m:
    m.write(f"The table of {n} is {str(table)}\n")
