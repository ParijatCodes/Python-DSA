#check if a student is pass or not
m1= int(input("Marks in Physics:"))
m2= int(input("Marks in Chemmistry:"))
m3= int(input("Marks in Math:"))
m4= int(input("Marks in Biology:"))

total_marks_percentage= (100*(m1+m2+m3+m4))/400

if(total_marks_percentage>=45 and m1,m2,m3,m4>=25):
    print('''Congrats!  You are Passed.
    \tYour Percentage is ''',total_marks_percentage,"%")
else:
    print("Sorry! You are failed")
