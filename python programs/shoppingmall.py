print("welcome to shopping mall")
cart=[]
prices=[]
bill=[]
while True:
    print("1.add item to cart,2.To know the bill,3.To items in cart,4.To remove the items")
    select=int(input("entr your option"))
    item=""
    if select==1:                                             

     while item!='ok':
          item=input("enter the item do you want")
          price=int(input("enter the price of the item"))
          prices.append(price)
          cart.append(item)
         # print(f"The list of items in cart is {cart}")  
         
         # print(f"The prices of item are {prices}") 
          break
    if select==2:
           while item!='ok':
                
             add=sum(prices)
             print(f"The total bill of your cart is {add}")   
             break
    if select==3:
           while item!='ok':
             print(f"The cart of items are {cart}")           
             print(f"The final prices of items {cart} and {prices}")
             break
    if select==4:
           while item!='ok':
               k=input("enter the item name do you want to remove")
               p=int(input("enter the price of item do you want to delete"))
               prices.remove(p)
               cart.remove(k)
               break
    if select==5:
              print("OOPs! You chossen worng option")