# class Employee:
#     fullname = "Empty"
#
#     def __init__(self, first, last, email):
#         ""
#         self.fullname = first + " " + last
#         self.set_email(email)
#     def get_email(self):
#         return self._email
#
#
# e1 = Employee("Roman", "Oliinyk", "jhdfb")
# e2 = Employee("Liubomyr", "Halamaha", "gvdfs")
#
# print(Employee.fullname)
# print(e1.fullname)
# print(e1.__class__.fullname)
#
# class Person:
#     def __init__(self, first_name="", last_name="", sex="male", age=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.age = age
#
#     def fullname(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"{self.fullname()} "
#
#
# class Employee(Person):
#     def __init__(self, first_name="", last_name="", sex="male", age=0, position=""):
#         super().__init__(first_name, last_name, sex, age)
#         self.position = position
#
#     def __str__(self):
#         return f"{self.fullname()} {self.position} "
#     def fullname(self):
#         return f"{self.first_name.upper()} {self.last_name.upper()}"
#     def old_fullname(self):
#         return super().fullname()
#
#
#
# e = Employee("Liubomyr", "Halamaha", "male", 36)
# print(e)
# print(e.fullname())
#
# class C(Employee):
#     def f(self):
#         super(Person).fullname()
#
#
# e = C("Liubomyr", "Halamaha", "male", 36, "pp")
# print(dir(e))
# print(e.last_name)
# print(e.f())


# class A:
#     def printA(self):
#         print("AA")
#
#     def printB(self):
#         print("AB")
#
#     def printC(self):
#         print("AC")
#
#     def printD(self):
#         print("AD")
#
#
# class B(A):
#     def printB(self):
#         print("BB")
#
#     def printC(self):
#         print("BC")
#
#     def printD(self):
#         print("BD")
#
#
# class C(A):
#     def printC(self):
#         print("CC")
#
#     def printB(self):
#         print("CB")
#
#     def printD(self):
#         print("CD")
#
#
# class D(B, C):
#     def printD(self):
#         print("DD")
#
#
# d = D()
# print(D.__mro__)
# d.printA()
# d.printB()
# d.printC()
# d.printD()
#
#
# class D(C, B):
#     def printD(self):
#         print("DD")
#
#
# d = D()
# print(D.__mro__)
# d.printA()
# d.printB()
# d.printC()
# d.printD()


# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(B): pass
# class F(C): pass
# class G(D): pass
# class K(E,F): pass
# class L(G,K): pass
# print(L.__mro__)

import math as m
m.pi

print(dir())

def f():
    print(dir())

f()