#MULTIPLICATION TABLE FROM 2 TO 20
def generateTable(n):
    table =""
    for i in range(1,11):
        table+= f"{n} x {i}= {n*i}\n"

        with open(f"q41MultiplicationTables/table_of_{n}.txt", "w") as t:
            t.write(table)
    

for i in range(2,21):
    generateTable(i)