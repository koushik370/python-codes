#This method is usually written "_" infront of  the funtion you want to write protect
class Protected_acess:
     def __init__(self):
          self._protected_variable="Protected Variable"
     def _protected_method(self):
           print("This is a protected method")
protected_obj=Protected_acess()
print(protected_obj._protected_variable)
protected_obj._protected_method()