# 1. В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку людини з Вашим віком.
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
# {other_person} is {older than / younger than / the same age as} me.

class Person():
    """My class person describe simple human"""

    def compare_age(self, your_age):
        if your_age > self.age:
            res_comp = "younger than"
        elif your_age < self.age:
            res_comp = "older than "
        else:
            res_comp = "the same age as"
        return f"{self.name} is {res_comp} me"

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1, p2, p3 = Person("Roman", 37), Person("Ruslan", 28), Person("Anna", 33)
my_age = 37
print(Person.__doc__)
print(p1.compare_age(my_age))
print(p2.compare_age(my_age))
print(p3.compare_age(my_age))

# 2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
# В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
# В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи ‘@company.com’ наприкінці.

class Employee():

    def __init__(self, first_name, last_name):
        self.fullname = first_name + " " + last_name
        self.email = first_name + "." + last_name + "@company.com"

    # def __str__(self):
    #     return f"{self.fullname=}, {self.email=}"

    def __repr__(self):
        return f"{self.fullname}, {self.email}"

emp1 = Employee("Roman", "Oleynik")
print(emp1.fullname)
print(emp1.email)
print(emp1)

# 3. В класі Name визначте:
# атрибути для first name та last name (fname та lname відповідно);
# атрибут fullname що повертає first і last names;
# атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name():

    def __init__(self, first_name, last_name):

        self.fname = first_name
        self.lname = last_name

    @property
    def fullname(self):
        return self.fname + " " + self.lname

    @property
    def initials(self):
        return self.fname[0] + "." + self.lname[0] + "."

    def __str__(self):
        return f"{self.fname}, {self.lname}, {self.fullname}, {self.initials}"

name1 = Name("Petro", "Mazur")
print(name1)