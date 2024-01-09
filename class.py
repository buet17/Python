# class x:
#     a=5
# # print(x.a)

# p1=x()
# print(p1.a)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("John",35)
# print(p1.name, end=", ")
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self,):
#         return  f"{self.name}({self.age})"
    
#     def x(self):
#         print("Hello my name is: " + self.name,self.age)
    
# p1=Person("John",35)
# print(p1)

# p1.x()

class baba:
    car='BMW'
    price='100 M'
    home='10th floor'

class child(baba):
    bike='R15'
    mobile='iphone 5'

class child2(child):
    laptop='HP'

p1=baba()
p2=child()
print(child.bike)
print(child.car)
# print(child.home)
print(child2.home)

del p1
del p2
#Done