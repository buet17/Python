# # class x:
# #     a=5
# # # print(x.a)

# # p1=x()
# # print(p1.a)

# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# # p1=Person("John",35)
# # print(p1.name, end=", ")
# # print(p1.age)

# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def __str__(self,):
# #         return  f"{self.name}({self.age})"
    
# #     def x(self):
# #         print("Hello my name is: " + self.name,self.age)
    
# # p1=Person("John",35)
# # print(p1)

# # p1.x()

# class baba:
#     car='BMW'
#     price='100 M'
#     home='10th floor'

# class child(baba):
#     bike='R15'
#     mobile='iphone 5'

# class child2(child):
#     laptop='HP'

# p1=baba()
# p2=child()
# print(child.bike)
# print(child.car)
# # print(child.home)
# print(child2.home)

# del p1
# del p2
# #Done

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
  