# This method is used to protect the code from third person 
# This method is mentioned "__" infront of funtion you want to make hide from others
#We cannot acess private funtion outside of class 
class Privte_Access:
    def __init__(self):
          self.__private_variable="Private variable"
    def __private_method(self):
          print("This is private method")
    def name_mangling(self):
            print(self.__private_method())
            print(self.__private_variable)
private_obj=Privte_Access()
private_obj.name_mangling()

