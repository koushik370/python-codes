#example on herarchical inheritance 
print("Representing the college daily currculam")
class College:
     def __init__(self,college_name,address
                  ):
          self.college=college_name
          self.address=address
          
     def college_details(self):
           print(f'The name of our college is {self.college} and address of our college is {self.address} ')
class Staff(College):
      def __init__(self,college,address,name,job):
             College.__init__(self,college,address)
             self.name=name
             self.job=job
             
      def staff_name(self):
             print(f"The name of staff is {self.name}") 
      def staff_job(self):
            print(f"The job of  {self.name}  is {self.job}")
      def staff_details(self):
             print(f'{self.job} and name is {self.name}')
      def college_details(self):
            return super().college_details()
class Students(College):
        def __init__(self,college,address,idno,name):
            College.__init__(self,college,address)
            self.idno=idno
            self.name=name

        def student_idnumber(self):
                print(f" The id number of student{self.name} id {self.idno} ")
        def student_college(self):
              return super().college_details()
Student_1=Students('chaithanya institue of technology and science','Naimnagar','e220083','koushik')
Staff_1=Staff('chaithanya clg','naimnagar','koushik','teaching')
Staff_1.staff_job()
Staff_1.college_details()
#.student_idnumber()
#Student_1.student_college()
