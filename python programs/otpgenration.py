import random
a=int(input("enter how many numbers do you want in password"))
b=int(input("enter how  many letters do you want in  password"))
c=int(input("enter how many symbols do you want in password"))
numbers=["1","2","3","4","6"]
letters=["a","b","c","d","e"]
symbols=["@","$","&"]
password=""
for i in range(0,a+1):

    rondom_choice=random.choice(numbers)
    password+=rondom_choice
for i in range(0,b+1):

   rondom_choice=random.choice(letters)
   password+=rondom_choice
for i in range(0,c+1):
    rondom_choice=random.choice(symbols)
    password+=rondom_choice
print("the password that you generated is ",password)    


