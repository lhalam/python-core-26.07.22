import subprocess
zenpy = subprocess.check_output('python -c "import this"', universal_newlines=True)
print(f"Кількість входження \n better: {zenpy.count('better')} \n never: {zenpy.count('never')} \n is: {zenpy.count('is')}\n"
      f"Всі великі літери: \n  {zenpy.upper()}'\n Замінені всі входження символу “і” на “&”: \n {zenpy.replace('i', '&')}")
z= (input("Введіть число: "))
dob=1
revers=[]
for number in z:
    revers.append(int(z)%10)
    dob*=int(z)%10
    z=int(z)/10
print(f'Добуток цифр:  {dob}')
t=(''.join([str(chisla) for chisla in revers]))
revers.sort()
sort=(''.join([str(chisla) for chisla in revers]))
print (f'Реверсний порядок: {t} \n Відсортовані цифри: {sort} ')
a=666
b=999
print (f'Значення двох змінних до заміни: а= {a} b= {b} \n')
a,b=b,a
print (f'Значення двох змінних після заміни: а= {a} b= {b} \n')