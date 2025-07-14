print("welcome to calculator")
while True:
       print("1.press one for additon")
       print("2.press two for subtraction")
       print("3.press three for multiplication")
       print("4.press four for division")
       select=int(input("enter the option do you want"))
       if select==1:
               while select!='ok':
                num_1=int(input("enter the first number"))
                num_2=int(input("enter the second number"))
                print("The additon of two numbers are",num_1+num_2)
                break
       if select==2:
                while select!='ok':
                        num_1=int(input("enter the first number"))
                        num_2=int(input("enter the second number"))
                        print("The subraction of numbers are",num_1-num_2)
                        break
       if select==3:
                while select!='ok':
                         num_1=int(input("enter the first number"))
                         num_2=int(input("enter the second number"))
                         print("The numltipication of two numbers are",num_1*num_2)
                         break
       if select==4:
                while select!='ok':
                          num_1=int(input("enter the first number"))
                          num_2=int(input("enter the second number"))
                          print("The division of two numbers are",num_1/num_2)
                          break
       
            
            