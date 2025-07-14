class Student:
    def __init__(self,add):
         print("calling from student class")
         self.admission=add
    def college(self):
          print("chaithanya deemmed to be university")
class Deatails :
      def __init__(self,name):
           print("calling from details class")
           self.name=name
      def home(self):
           return f"Student name is  {self.name}"  
class Both(Student,Deatails):
     def __init__(self,name,add):
      Student.__init__(self,add)
      Deatails.__init__(self,name)
     def data(self):
           print(f"The student name is {self.name} and addimission number is {self.admission} and belongs to ")      
student_1=Both("koushik","E220083")   
student_1.data()