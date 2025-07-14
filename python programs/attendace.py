# program on attendece in collage and what people should acess those attendence
print("CHAITANYA INSTITUTE AND TECHNOLOGY OF SCIENCE")
class Student:
     def __init__(self,adm):
           self.adm=adm
     def  addmission_number(self):
            print(f"Addmission number of student is {self.adm}")
class Teacher(Student):
       def __init__(self,adm,section):
        Student.__init__(self,adm)
        self.section=section
       def student_section(self):
             print(f"The student is belongs to {self.section}")
class Principle(Teacher):
       def __init__(self,adm,name,section):
           Teacher.__init__(self,adm,section)
           self.name=name
       def student_name(self):    
            print(f"The name of student is {self.name} and belongs to {self.section} section")
       def addmission_number(self):
             print(f"tThe admission number of student is {self.adm} of {self.name}")
Student_1=Student('E220083')
Student_1=Principle('E220083','koushik','A1')
Student_2=Principle("E220084",'anji reddy','A1')
Student_1.student_name()
Student_2.student_name()
Student_1.addmission_number()
Student_2.addmission_number()
            
    
                    

                  
                  
    