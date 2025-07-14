class Student:
 def __init__(self,name,address):
     self.name=name
     self.address=address
 def gender(self):
     print("He is a male")
 def  _gender(self):
     print("She is a female")
display=Student('koushik',"Bhupalapally")
print(display.name)
display._gender()