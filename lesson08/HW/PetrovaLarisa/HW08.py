class Person:
    def __init__(self, name="", age = 0):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name=}"
    def compare_age(self, other_person):
        if self.age < other_person.age:
            return f"{other_person} is older than me"
        elif self.age > other_person.age:
            return f"{other_person} is younger than me"
        else:
            return f"{other_person} is the same age as me"

me = Person("Larisa", 37)
p1 = Person("Anna", 19)
p2 = Person("Sam", 45)
p3 = Person("Val", 37)
print(me.compare_age(p1))
print(me.compare_age(p2))
print(me.compare_age(p3))

class Employee:
    def __init__(self, first_name="", last_name= ""):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = self.first_name + " " + self.last_name
        l = [self.first_name, self.last_name, ]
        self.email = (".").join(l) + "@company.com"
    def __str__(self):
        return f"{self.fullname=} {self.email=}"

e1 = Employee("John", "Smith")
e2 = Employee("Barbara", "Straisand")
print(e1)
print(e2)

class Name:
    def __init__(self, fname="", lname= ""):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + " " + self.lname
        self.initials = self.fname[0] + "." + self.lname[0]
    def __str__(self):
        return f"{self.fullname=} {self.initials=}"

n1 = Name("John", "Smith")
n2 = Name("Barbara", "Straisand")
print(n1)
print(n2)