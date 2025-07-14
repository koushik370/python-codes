#program to show hybrid inheritance
class Plant:
     def __init__(self,name):
           self.name=name
     def plant_name(self):
            print(f" the name of plant is {self.name}")
class  Food(Plant):
       def __init__(self,name,intake):
              self.intake=intake
              Plant.__init__(self,name)
              
       def plant_food(self):
              print(f"the {self.name} food is {self.intake}")
       def plant_name(self):
               return super().plant_name()
class Study:
        def __init__(self,study):
                self.study=study
        def plant_study(self):
                print(f" The study of plant is called {self.study}")
class About_plant(Food,Study):
        def __init__(self,name,intake,study):
               Food.__init__(self,name,intake)
               Study.__init__(self,study)
        def about_plant(self):
                print(f" The name is {self.name} and study is {self.study} and they consume {self.intake} ")
class Summery(About_plant):
         def __init__(self,name,intake,study,status):
                About_plant.__init__(self,name ,intake,study) 
                self.status=status
         def about_plant(self):
                return super().about_plant()
         def plant_status(self):
                 print(f"According to my knowledge the plant is {self.status}")
plant_1=Summery('cactus','insects','unkonwn','Good')
plant_2=About_plant('kalamanda','water','unknown')
plant_2.about_plant()
print(plant_1.study)

       


               
         
              


             