'1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини з Вашим віком.'
'При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:'
'{other_person} is {older than / younger than / the same age as} me'

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age > other_person.age:
            print(f"{other_person.name} is younger than me.")
        elif self.age < other_person.age:
            print(f"{other_person.name} is older than me.")
        else:
            print(f"{other_person.name} is the same age as me.")

me = Person('Pavel', 27)
p1, p2, p3 = Person('Fus', 26), Person('Ro', 27), Person('Dah', 28)
# me.compare_age(p1), me.compare_age(p2), me.compare_age(p3)

"""2.   Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
   - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
   - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи  ‘@company.com’ наприкінці."""

class Employee:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.full_name = f_name + ' ' + l_name
        self.email = f_name + '.' + l_name + '@company.com'

    def __str__(self):
        return f'{self.full_name} has email {self.email}'

me_v2 = Employee('Pavel', 'Ivanov')
# print(me_v2)

'''3. В класі Name визначте:
    - атрибути для first name та last name (fname та lname відповідно);
    - атрибут fullname що повертає first і last names;
    - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’)'''

class Name:

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.fullname = self.fname + ' ' + self.lname
        self.initials = first_name[0] + '.' + last_name[0]

me_v3 = Name('Pavel', 'Ivanov')
# print(f"Fullname: '{me_v3.fullname}'\nInitials: '{me_v3.initials}'")