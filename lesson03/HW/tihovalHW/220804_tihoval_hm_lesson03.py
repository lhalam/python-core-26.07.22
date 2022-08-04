import contextlib
import io
import math as m

with contextlib.redirect_stdout(zen_temp := io.StringIO()):
    import this
zen = zen_temp.getvalue()
print(zen)

is_count = zen.count('is')
better_count = zen.count('better')
never_count = zen.count('never')

print('Task 1')
print('\nnever: ', never_count, '\nbetter: ', better_count, '\nis: ', is_count)
print(zen.upper())
print(zen.replace('i', '&'))

i = 1534
print(i)
i_list = [int(i) for i in str(i)]
print('Product:\t', m.prod(i_list))
i_list.reverse()
print('Reverse:\t', ''.join([str(i) for i in i_list]))
i_list.sort()
print('Sort:\t\t', ''.join([str(i) for i in i_list]))

a = 123
b = 345
print('a = ', a, '\nb = ', b)
print(id(a))
print(id(b))

a, b = b, a

print('a = ', a, '\nb = ', b)
print(id(a))
print(id(b))