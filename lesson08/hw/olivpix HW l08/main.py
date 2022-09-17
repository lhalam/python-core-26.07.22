# 1. В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку людини з Вашим віком.
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення
# наступного формату: {other_person} is {older than / younger than / the same age as} me.
class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def compare_age(self, user_age):
        if self.age > user_age :
            return f"{self.name} is older than me"
        elif self.age == user_age:
            return f"{self.name} the same age as me"
        else:
            return f"{self.name} is younger than me"


user_age = int(input("Enter your age: "))
p1 = Person("Max", 75)
p2 = Person("Andre", 17)
p3 = Person("Mari", 23)

print(p1.compare_age(user_age))
print(p2.compare_age(user_age))
print(p3.compare_age(user_age))

# 2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#  - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#  - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи ‘@company.com’ наприкінці.

class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name}.{last_name}@company.com"

p1 = Employee("Oliver", "Pix")
print(p1.fullname)
print(p1.email)

# 3. В класі Name визначте:
# - атрибути для first name та last name (fname та lname відповідно);
# - атрибут fullname що повертає first і last names;
# - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = f"{fname} {lname}"
        self.initials = f"{fname[0]}.{lname[0]}."

p1 = Name("Oliver", "Pix")
print(p1.fullname)
print(p1.initials)

