#Ducktyping  is one of the method in polymorphism which is used set data in dynamic state
class Duck:
     def swim(self):
           print("Iam a duck i can swim")
     def voice(self):
            print(" I can sound like duck")
class Dog:
       def swim(self):
              print("Iam dog so i can swim partially")
       def voice(self):
               print("I can bark")
class Cat:
        def swim(self):
                print("Iam a cat so i cannot swim")
        def voice(self):
                print("I sound like meow meow")
def display(obj):
       obj.swim()
       obj.voice()
       print("information displayed")
Duck_1=Duck()
dog_1=Dog()
cat_1=Cat()
display(Duck_1)