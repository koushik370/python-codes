def check(n,m):
     a=0
     b=1
     for i in range(e,r+1):
          c=a+b
          a=b
          b=c
          print(c)
e=int(input("enter the starting number")) 
r=int(input("enter the ending number")) 
check(e,r)        