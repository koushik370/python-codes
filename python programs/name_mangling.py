class Private_Access:
     def __init__(self,name,mole,weight):
          self.__name=name
          self.__mole=mole
          self.__weight=weight

     def  __person_name(self):
           print("The name of person is ",self.__name)
     def __person_mole(self):
           print(f"{self.__name} person has mole on {self.__mole}")
     def __person_weight(self):
            print(f"{self.__name} is {self.__weight} of kgs")
person_1=Private_Access("koushik","A mole on the right plam",58)
person_1._Private_Access__person_name()
person_1._Private_Access__person_mole()
person_1._Private_Access__person_weight()

        