# class MyContextManager:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print(f'{self.name} entered')
#         return self.name
#
#     def __exit__(self, *args):
#         print(f'{self.name} exited')
#         if args[0]:
#             print(f'but with {args[0].__name__} with name {args[1]}')
#
#
# pcm1 = MyContextManager('context manager 1')
# pcm2 = MyContextManager('context manager 2')


# with pcm1 as name:
#     print(f'in with block for {name}')
#
# try:
#     with pcm2 as name:
#         raise Exception("My error")
#         print(f'in with block for {name}')
# except:
#     print(f'Error occurred.')


# file = open('welcome.txt', 'a')
# try:
#     file.write('hello world')
# finally:
#     file.close()

#
# with open('welcome.txt', 'a') as file:
#     file.write(" WITH ")

#
# with open('welcome.txt', 'r') as file:
#     text = file.read()
#     print(text)
#
# with open('welcome.txt', 'r') as file:
#     text = file.readline()
#     print(text)
#     for line in file:
#         print(line)

#
# @contextmanager
# def managed_file(name, method):
#     f = open(name, method)
#     try:
#         print("start managed_file")
#         yield f
#     finally:
#         f.close()
#         print("end managed_file")
#
#
# with managed_file('hello.txt', 'w') as f:
#     print("start")
#     f.write('hello, world!')
#     f.write('bye now')
#     print("end")

class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"{self.first_name}{self.last_name}"


class Team(object):
    def __init__(self, students):
        self.students = students

    @classmethod
    def from_json(cls, data):
        students = list(map(Student.from_json, data["students"]))
        return cls(students)


student1 = Student(first_name="Jake", last_name="Foo")
student2 = Student(first_name="Jason", last_name="Bar")
team = Team(students=[student1, student2])
team2 = Team(students=[student1, student2])
# Serializing
import json

l = [team2, team]

data = json.dumps(l, default=lambda o: o.__dict__, sort_keys=True, indent=4)

print(data)

data = json.dumps(team, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print(data)
# Deserializing
decoded_team = Team.from_json(json.loads(data))
print(decoded_team)
print(decoded_team.students)
