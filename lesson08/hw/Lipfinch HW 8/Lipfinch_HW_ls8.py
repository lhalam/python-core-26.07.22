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







