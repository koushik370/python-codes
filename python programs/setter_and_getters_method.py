class Private_Access:
     def __init__(self,name_1,name_2,religion_1,religion_2,relatonship):
           self.__boy_name=name_1
           self.__girl_name=name_2
           self.__caste_1=religion_1
           self.__caste_2=religion_2
           self.__boyfriend=relatonship
     def get__boyname(self):
            print(f"The name of the boy is {self.__boy_name}")
     def get__girlname(self):
            print(f"The name of girl is {self.__girl_name}")
     def get__boy_caste(self):
           print(f"The {self.__boy_name} is belongs to {self.__caste_1} caste")
     def get__girl_caste(self):
            print(f"The caste of {self.__girl_name} is {self.__caste_2}")
     def get__relation(self):
            print(f"{self.__boy_name} and {self.__girl_name} are in {self.__boyfriend}")
survey_1=Private_Access("anji" ,"sowmya",'OC','BCD','attraction')
survey_1.get__boyname()
survey_1.get__girlname()
survey_1.get__boy_caste()
survey_1.get__girl_caste()
survey_1.get__relation()

            