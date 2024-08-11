class car:
   def __init__(self) -> None:
      pass
   def myclass():
      global abc
      abc=10

   def myclass2():
    #   print(abc)
        print("inside myclass2")

car.myclass() #Set the global variable
# car.myclass2()


class car2:
   def car2_fun():
      print("abc value from car2 class function:-",abc)

car2.car2_fun()


   