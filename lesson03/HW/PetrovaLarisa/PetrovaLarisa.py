import this
import codecs

zen_of_python = codecs.encode(this.s, 'rot13')
print('Number of occurrence of "better":', zen_of_python.count('better'))
print('Number of occurrence of "never":', zen_of_python.count('never'))
print('Number of occurrence of "is":', zen_of_python.count('is'))
print(zen_of_python.upper())
print(zen_of_python.replace("i", "&"))
number = 1254
num_to_str = str(number)
dob = int(num_to_str[0])*int(num_to_str[1])*int(num_to_str[2])*int(num_to_str[3])
print(f'Число - {number}, добуток його цифр - {dob}.')
print(num_to_str[::-1])
num_to_list = list(num_to_str)
num_to_list[0] = int(num_to_list[0])
num_to_list[1] = int(num_to_list[1])
num_to_list[2] = int(num_to_list[2])
num_to_list[3] = int(num_to_list[3])
num_to_list.sort()
print(num_to_list)
a = 50
b = 10
print(f'a = {a}, b = {b}')
a = a + b
b = a - b
a = a - b
print(f'a = {a}, b = {b}')