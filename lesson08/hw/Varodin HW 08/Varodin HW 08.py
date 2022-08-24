# Task 1

class Person:
    def __init__(self, p1, p2):
        self.name = p1
        self.age = p2
        self.my_age = 35

    def compare_age(self):
        if self.age > self.my_age:
            return  f'{self.name} is older than me.'
        if self.age < self.my_age:
            return  f'{self.name} is younger than me.'
        if self.age == self.my_age:
            return  f'{self.name} is the same age as me.'


a = Person('Alex', 35)
print(a.compare_age())

# Task 2

class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = f'{first_name} {last_name}'
        self.email = f'{first_name}.{last_name}@company.com'

b = Employee('Alexandr','Varodin')
print(b.fullname)
print(b.email)

# Task 3

class Name:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.fullname = f'{fname} {lname}'
        self.initials = f'{fname[0]}.{lname[0]}'

c = Name('Alexandr', 'Varodin')
print(c.first_name)
print(c.last_name)
print(c.fullname)
print(c.initials)


