from abc import ABC,abstractmethod
class Vechile (ABC):
     def __init__(self,n):
           self.n=n
     @abstractmethod
     def start(self):
            pass
     def display(self):
           print("Hi iam calling from vechile classs")
class Bike(Vechile):
       def __init__(self,n,colour):
              Vechile.__init__(self,n)
              self.colour=colour
       def start(self):
              print("Start with kick")
class Scooty(Vechile):
       def __init__(self,n):
              Vechile.__init__(self,n)
       def start(self):
               print("start with self")
              
class Car(Vechile):
        def __init__(self,n):
            Vechile.__init__(self,n)
            self.gears=6
        def start(self):
               print("Start with key")
Vechile_1=Vechile(2)
Vechile_1.start()
Vechile_1.display()
 


        
