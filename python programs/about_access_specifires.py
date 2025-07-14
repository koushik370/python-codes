# This method is used to protect the code from third person 
# This method is mentioned "__" infront of funtion you want to make hide from others
#We cannot acess private funtion outside of class 
#We can also access private data outside the class by using three techniques
#1.name_mangling
#2.Defining the public funtion inside the data
#3.By using getters and setters method in the code or programe

'''import class_in_class as p #By using  class in class method 
print(p.Privte_Access())'''

'''import name_mangling as n #By using name_mangling method 
print(n.Private_Access)'''

import setter_and_getters_method as g
print(g.Private_Access)