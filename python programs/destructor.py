#1.Destructor method is useful to delete funtion 


class Person:
     def __del__(self,name,age):
           self.name=name
           self.age=age
     def display(self):
            print(f"Name is {self.name} and age is {self.age}")
     def __del__(self):
            print(f"{self.name} has been destroyed")
john=Person("koushik",19)
del john
john.display()

           