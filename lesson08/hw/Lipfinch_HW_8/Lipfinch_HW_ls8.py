# 1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини з Вашим віком.
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
# {other_person} is {older than / younger than / the same age as} me.

class Person:
    def __init__(self, first_name = '', age = 0):
        self.name = first_name
        self.age = age
    def compare_age(self, other_person):
        if self.age < other_person.age:
            return f'other person older than me'
        elif self.age > other_person.age:
            return f'other person is younger than me'
        else:
            return f'we same age'
me = Person('Eugene', 32)
p1 = Person('Clara', 31)
p2 = Person('Adam,', 26)
p3 = Person('Alex', 35)
print(me.compare_age(p1)), print(me.compare_age(p2)), print(me.compare_age(p3))

# 2.   Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#    - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#    - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи  ‘@company.com’ наприкінці.

class Empoyee:
    def __init__(self, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.email = first_name + '.' + last_name + '@company.com'
    def __str__(self):
        return f'Emplpoyee:  {self.full_name} has email {self.email}'

p1 = Empoyee('Eugene', ' Svyrydenko')
print(p1)

#3. В класі Name визначте:
   # - атрибути для first name та last name (fname та lname відповідно);
   # - атрибут fullname що повертає first і last names;
   # - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + lname
        self.initials = fname[0] + '.' + lname[0]
    def __str__(self):
        return f'Full name:{self.fullname}, and his initials are {self.initials}'

p2 = Name("Eugene ", "Svyrydenko")
print(p2)





