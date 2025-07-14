'''1.Construtor method is useful to define the class and class objects 
2.Constructor again classified into two types they are
*parameterized constructor
*non_parameterized constructor '''
 
#parameterized constructor
'''class Myclass:
     def __init__(self):
            print("Hello")
obj=Myclass()'''

#non_parameterized constructor
'''class Person:
       def __init__(self,name,hobby):
              self.name=name
              self.hobby=hobby
       def display(self):
               print(f"The name of the person is {self.name} and the person has  {self.hobby} as hobby")
details_1=Person('koushik','playing cricket')
details_1.display()'''