''' conditional statments are of four types
1.if condition
2.nestedif condition
3.elif conditon
4.if else condition'''


name=input("enter the name of the person")
age=int(input("enter the age of the person"))
if(age<=18):
      print(f"{name} your are not eligible for vote")
else:
      print(f"{name} your are eligible for vote")
      print("please dont forget to caste your vote")
print("Thanks for using")