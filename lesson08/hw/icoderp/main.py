# 1. В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку
# людини з Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
# буде повертатися повідомлення наступного формату: {other_person} is {older than / younger than / the same age as} me.

# class Person:
#     __my_name = "Ivan"
#     __my_age = 14
#
#     def compare_age(self, name, age):
#         if self.__my_age > age:
#             print(f"{name} is younger than me.")
#         elif self.__my_age < age:
#             print(f"{name} is older than me.")
#         elif self.__my_age == age:
#             print(f"{name} is the same age as me.")
#
#
# p1 = Person()
# p2 = Person()
# p3 = Person()
#
# p1.compare_age('Tom', 44)
# p2.compare_age('Mick', 13)
# p3.compare_age('Jon', 14)

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

