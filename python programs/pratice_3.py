class Adding:
     def __init__(self,name,age):
           self.name=name
           self.age=age
     def person_name(self):
             print(f"The name of person is {self.name}")
     def person_age(self):
             print(f"The age of person is {self.age}")
     def __add__(self,other):
             return f" The enter name afer combining {self.name + other.name}  and the total name after combining {self.age + other.age}"
info_1=Adding('koushik',19)
info_2=Adding('Reddy',17)
print(info_1+info_2)