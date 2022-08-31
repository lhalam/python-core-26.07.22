print("Task 1")


class Person:
    def __init__(self, first_name = '', age = 0):
        self.name = first_name
        self.age = age

    def compare_age(self, other_person):
        if self.age < other_person.age:
            return f'Other person is older than me'
        elif self.age > other_person.age:
            return f'Other person is younger than me'
        else:
            return f'We are the same age'


me = Person('Joseph', 21)
p1 = Person('Simon', 21)
p2 = Person('Petrograd,', 19)
p3 = Person('Alexa', 26)
print(me.compare_age(p1)), print(me.compare_age(p2)), print(me.compare_age(p3))


print("Task 2")


class Employee:
    def __init__(self, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.email = first_name + '.' + last_name + '@company.com'

    def __str__(self):
        return f'Employee:  {self.full_name} has email {self.email}'


p1 = Employee('Joseph', 'Ushkin')
print(p1)


print("Task 3")


class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + lname
        self.initials = fname[0] + '.' + lname[0] + '.'

    def __str__(self):
        return f'Full name:{self.fullname}, and his initials are {self.initials}'


p2 = Name("Joseph ", "Ushkin")
print(p2)