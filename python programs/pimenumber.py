a=int(input("enter the first interval"))
b=int(input("enter the second interval"))
for num in range(a,b+1):
     if num>1:
       for i in range(2,num):
              if num%i==0:
               break
       else: 
             print(num)   




            