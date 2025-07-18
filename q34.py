#farhenhite to celsius convertion
def c_to_f(f):
    return 5*(f-32)/9
f= int(input("Write the temp in F: "))
c= c_to_f(f)
print(f"{round (c, 2)} degree C", )