# l = [1,2,3]
# sorted(l)
# l.sort()
#
# class Person:
#     first_name = ""
#     last_neme = ""
#     age = 0
#     parent = []
#     def __init__(self, first_name = "", last_neme="", sex="male"):
#         self.first_name = first_name
#         self.last_neme = last_neme
#         self.sex = sex
#     def __str__(self):
#         return f"{self.first_name=} {self.last_neme=} {self.age=} {self.parent=}"
#
#
#
#
# p1 = Person()
# p2 = Person()
# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)
#
# p1.first_name = "A"
# p2.last_neme = "B"
# print(p1.__dict__)
# print(p2.__dict__)
# print(p1)
# print(p2)
# Person.age = 20
# print(p1)
# print(p2)
# p1.parent.append("p1")
# p2.parent.append("p2")
# Person.parent.append("class")
# print(p1)
# print(p2)
# print(p1.__dict__)
# print(p2.__dict__)
# import random
#
#
# class Person:
#     population = []
#
#     def __init__(self, first_name="", last_name="", sex="male", age=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.age = age
#         self.population.append(self)
#         self.beloved = None
#         self.father = None
#         self.heve = None
#
#     def __str__(self):
#         return f"first_name: {self.first_name}\n" \
#                f"last_name: {self.last_name}\n" \
#                f"age: {self.age=}\n" \
#                f"sex: {self.sex=}\n" \
#                f"father: {self.father=}\n" \
#                f"heve: {self.heve=}\n" \
#                f"beloved: {self.beloved}\n"
#
#     def __repr__(self):
#         return f"<{self.first_name} {self.last_name} {self.age} {self.sex}>"
#
#     def add_my_half(self, half):
#         self.beloved = half
#
#     # def __add__(self, other):
#     #     children = Person()
#     #     children.sex = "male" if random.randint(1, 100) % 2 else "female"
#     #     if self.sex == "male":
#     #         children.father = self
#     #         children.heve = other
#     #         children.last_name = self.last_name
#     #     else:
#     #         children.father = other
#     #         children.heve = self
#     #         children.last_name = other.last_name
#     #     return children
# def new_children(p1, p2):
#     children = Person()
#     children.sex = "male" if random.randint(1, 100) % 2 else "female"
#     if p1.sex == "male":
#         children.father = p1
#         children.heve = p2
#         children.last_name = p1.last_name
#     else:
#         children.father = p2
#         children.heve = p1
#         children.last_name = p2.last_name
#     return children
#
# p1 = Person("pablo", "zoro", "male", age=33)
# p2 = Person("ana", "popva", "female", age=18)
# # print(p1)
# # print(p2)
# # print(p1.population)
# p1.add_my_half(p2)
# # print(p1)
# # print(p2)
# # p3 = p1+p2
# # p4 = p2+p1
# p3 = new_children(p1, p2)
# p4 = new_children(p2, p1)
# print(p3)
# print(p4)
# Person.generate_new_children = new_children
# Person.__add__ = new_children
# p3 = p1.generate_new_children(p2)
# p4 = p2.generate_new_children(p1)
# print(p3)
# print(p4)
# p3 = p1+p2
# p4 = p2+p1


# class Singleton(object):
#     obj = None  # attribute for storing a single copy
#
#     def __new__(cls, *dt, **mp):  # class Singleton.
#         if cls.obj is None:
#             # If it does not yet exist, then
#             # call __new__ of the parent class
#             cls.obj = object.__new__(cls, *dt, **mp)
#         return cls.obj  # will return Singleton
#
# s1 = Singleton()
# s2 = Singleton()
# s3 = Singleton()
# print(s1)
# print(s2)
# print(s3)

# class A:
#     def inst(self):
#         print("inst", type(self))
#
#     @classmethod
#     def class_method(cls):
#         print("class_method", type(cls))
#
#     @staticmethod
#     def class_method():
#         print("class_method")
#
#
# a = A()
# a.inst()
# a.class_method()
# A.class_method()

# class __A():
#     def __init__(self):
#         self.pub = "pub"
#         self._pro = "pro"
#         self.__pri = "pri"
#
#
# a = __A()
# print(a.pub)
# print(a._pro)
# print(a._A__pri)

class Human:
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("must by positive")
    # age = property(get_age, set_age)
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("must by positive")



h = Human()
print(h.get_age())
h.set_age(-18)
print(h.get_age())
h.set_age(5)
print(h.get_age())
print(h.age)
h.age = -15
h.age = 15

print(h.age)




