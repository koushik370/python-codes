''' conditional statments are of four types
1.if condition
2.nestedif condition
3.elif conditon
4.if else condition'''


number=int(input("enter the number"))
if(number>=0):
    if(number==0):
         print("the number is zero")
    else:
         print("the number is positive")
else:
    print("the number is negative")
print("execution completed")