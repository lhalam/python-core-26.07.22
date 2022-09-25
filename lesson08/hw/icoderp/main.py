# 1. В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку
# людини з Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
# буде повертатися повідомлення наступного формату: {other_person} is {older than / younger than / the same age as} me.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, person):
        if self.age > person.age:
            print(f"{person.name} is younger than me.")
        elif self.age < person.age:
            print(f"{person.name} is older than me.")
        elif self.age == person.age:
            print(f"{person.name} is the same age as me.")


p1 = Person('Tom', 44)
p2 = Person('Mick', 13)
p3 = Person('Jon', 14)

p1.compare_age(p2)
p1.compare_age(p3)
p2.compare_age(p1)
p2.compare_age(p3)
p3.compare_age(p1)
p3.compare_age(p2)

# 2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
# В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
# В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи ‘@company.com’ наприкінці.

# class Employee:
#     fullname = ''
#     email = ''
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.fullname = f'{first_name} {last_name}'
#         self.email = f'{first_name}.{last_name}@company.com'
#
#
# e = Employee('Jon', 'Sina')
# print(f"{e.fullname} - {e.email}")

# 3. В класі Name визначте:
# атрибути для first name та last name (fname та lname відповідно);
# атрибут fullname що повертає first і last names;
# атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

# class Name:
#     fname = ''
#     lname = ''
#     fullname = ''
#     initials = ''
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.fname = first_name
#         self.lname = last_name
#         self.fullname = f'{first_name} {last_name}'
#         self.initials = f'{first_name[0]}.{last_name[0]}'
#
#
# n = Name('Jon', 'Sina')
# print(f"{n.fname=}, {n.lname=}, {n.fullname=}, {n.initials=}")
