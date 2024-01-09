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

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self,):
        return  f"{self.name}({self.age})"
    
p1=Person("John",35)
print(p1)
