print("Welcome to koushik shopping mall")
l=[]
v=[]
n=[]
while True:
     print("1.To add elements in the cart")
     print("2.To veiw the price of the item added")
     print("3.To know the bill of the cart")
     print("4.To remove any item from your list")
     print("5.To view removed items inthe list")
     option=int(input("Enter your option"))
     if option==1:
           while option!="ok":
             item=input("enter the item name that your want to add")
             price=int(input("enter the price of the item "))
             v.append(price)
             l.append(item)
             break
     if option==2:
            while option!="ok":
                  print(f"The items are {l} and price of items are {v}")
                  break
     if option==3:
            while option!="ok":
                   total_bill=sum(v)
                   print(f"The total bill of your cart id {total_bill}")
                   break
     if option==4:
             while option!="ok":
                    item_remove=input("enter the item should be removed")      
                    item_price=int(input("enter the price of item with respective item you want to remove"))
                    l.remove(item_remove)
                    v.remove(item_price)
                    break
             
            
          

     