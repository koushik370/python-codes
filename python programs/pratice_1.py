class Male:
     def __init__(self,b_name,b_hobby):
           self.b_name=b_name
           self.b_hobby=b_hobby
           self.eyes=2
     def name_boy(self):
            print(f" The name of boy is {self.b_name}")
     def boy_hoobies(self):
            print(f" The boy  hobbies are {self.b_hobby}")
class Female:
       def __init__(self,g_name,g_hobby):
             self.g_name=g_name
             self.g_hobby=g_hobby
             self.eyes=2
       def  girl_name(self):
              print(f"The name of girl is {self.g_name}")  
       def  girl_hobby(self):
              print(f"The hobbies of girl is {self.g_hobby}")  
class Both(Male,Female):
        def __init__(self,b_name,b_hobby,g_name,g_hobby):
               Male.__init__(self,b_name,b_hobby)
               Female.__init__(self,g_name,g_hobby)
        def combine(self):
                print(f" The name of boy is {self.b_name}  and the  hobbies are {self.b_hobby} name of girl is {self.g_name}  and the girl hobbies are {self.g_hobby}  ")  
Set_1=Both('koushik','playing cricket','varshini','watching movies')   
Set_1.combine()                  
                    

