from abc import ABC,abstractmethod
class Shape_interface(ABC):
    @abstractmethod
    def cal_area(self):
         pass
class Reactangle(Shape_interface):
      def __init__(self,length,bridth):
            self.length=length
            self.bridth=bridth
      def cal_area(self):
            print("The area of reactangle is :",self.length*self.bridth)
class Circle(Shape_interface):
      def __init__(self,radius):
             self.radius=radius
             self.pi=3.14
      def cal_area(self):
            print("The area of circle is :",self.pi*self.radius**2)
class Triangle(Shape_interface):
      def __init__(self,length,bredth,hieght):
            self.length=length
            self.bredth=bredth
            self.hieght=hieght
      def cal_area(self):
             print("The area of triangle is :",self.length*self.bredth*self.hieght)
class Squre(Shape_interface):
      def __init__(self,side):
            self.side=side
      def cal_area(self):
             print("The area of square is :",self.side*self.side)
shape_1=Triangle(5,2,1)
shape_1.cal_area()
shape_2=Circle(5)
shape_2.cal_area()
shape_3=Reactangle(5,2)
shape_3.cal_area()
shape_4=Squre(5)
shape_4.cal_area()