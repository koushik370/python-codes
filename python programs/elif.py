''' conditional statments are of four types
1.if condition
2.nestedif condition
3.elif conditon
4.if else condition'''

''' Q what is the difference between elif and if stament
    A:-elif statment is written where the multiple conditons not checked but in
      if statement it checks all conditons if first conditon is true
'''
marks=int(input("enter the marks of student to know the percentage of the student"))
if(marks>=90):
      print(f"The student scored{marks} in exam and awarded A grade")
      print(f"{marks/95*100}% is the percentage of the student ")
elif(marks>=80):
      print(f"The student scored {marks} in exam and awareded B grade in exam")
      print(f"{marks/95*100}% is the percentage of the student ")
elif(marks>=70):
       print(f"The student scored {marks} in exam and awareded C grade in exam ")
       print(f"{marks/95*100}% is the percentage of the student ")
elif(marks<=60):
       print(f"The student scored {marks} in exam")
       print(f"There is no percentage for the student who scores {marks} in exam")
       
       