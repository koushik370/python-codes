class Human:
    def eat(self):
         print("I can eat")
    def work(self):
          print("I can work")
class Male(Human):
      def sleep(self):
            Human.eat(self)
            print("I can sleep whole day")
class Boy(Male):
       def work(self):
         Human.work(self)
         print("I can code ")
boy_1=Boy()
boy_1.sleep()