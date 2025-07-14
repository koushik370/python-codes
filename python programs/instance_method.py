class Person: #instance method in object oriented language
     def __init__(self,name,age):
           self.name=name
           self.age=age
     def say_hello(self):
             print(f"Hello my name is {self.name} and iam {self.age} years old")
person_1=Person("jonh",19)
person_1.say_hello()

class Person:
       country="India"
       @classmethod
       def info(cls):
               return cls.country
print(Person.info())
sachine=Person()
print(sachine.info)
