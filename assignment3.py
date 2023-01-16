# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:13:04 2022

@author: Pritish

ASSIGNMENT --III
"""

#1
n=int(input('n= '))
print('sum of square of the number:',sum([i**2 for i in range(n+1)]))
print('sum of cube of the number:',sum([i**3 for i in range(n+1)]))

print('$ sum of square of the number:',n*(n+1)*(2*n+1)/6)
print('$ sum of square of the number:',n**2*(n+1)**2/4)

print('----------------------------------------')
#2
n1=int(input('length of the list, n= '))
i=1
l_1=[]
while len(l_1)<n1:
    l_1.append(i)
    i+=2
    if len(l_1)==n1:
        break
    l_1.append(0)
print(l_1)

print('----------------------------------------')
#3
n=int(input("length of the list, n= "))
Sn=[]
for i in range(1,n+1):
    l1=list(range(1,i+1))
    l2=[k**2 for k in l1]
    Sn.append(sum(l2))
print('the list is:',Sn)

print('----------------------------------------')
#4
n=int(input('n= '))
p=1
for i in range(n+1):
    m=1+i/p
    p=m
print('required value:',m)

print('----------------------------------------')
#5
n=int(input('n= '))
f=[1,1]    
if n>2:
    for i in range(3,n+1):
        f.append(f[i-3]+f[i-2])
    print('the fibonacci series:',f)    
else:
    print('the fibonacci series:',f[:n])

print('----------------------------------------')
#6
while True:
    q=float(input('enter a number: '))
    if q>=0:
        print('the sqrt of the number:',q**(1/2))
        break
    else:
        print('ERROR--invalid input:',q)
        continue

print('----------------------------------------')
#7
#7.1
name=str(input('name of student: '))
age=float(input('age of student: '))
tup1=(name,age)
print('tuple is:', tup1)

#7.2
lt=[]
for i in range(10):
    name=str(input(f'name of student {i+1} : '))
    age=float(input(f'age of student {i+1} : '))
    tup1=(name,age)
    lt.append(tup1)
print('list of tuples',lt)

#7.3
name1=str(input('enter a name: '))
for i in range(len(lt)):
    if name1 in lt[i]:
        print(f'age of {name1} :',lt[i][1])

print('----------------------------------------')
#8
n=list(str(input('enter phone number: ')))
ph=[eval(i) for i in n]
w=list(range(10))
for j in ph:
    if j in w:
        w.remove(j)
print('digit absent in phone number',w)

print('----------------------------------------')
#9
ids=[143,172,139,220,36,150,169,211,189,9,68,122,101]
rollnos=[]
for i in range(len(ids)):
               if len(str(ids[i]))==1 :
                   rollnos.append('21MS00'+str(ids[i]))
               elif len(str(ids[i]))==2 :
                   rollnos.append('21MS0'+str(ids[i]))
               else:
                   rollnos.append('21MS'+str(ids[i]))
print('list of roll numbers',rollnos)
print('Group_A =', [j for j in rollnos if int(j[4:])<150])
print('Group_B =', [j for j in rollnos if int(j[4:])>=150])

print('----------------------------------------')
#10
farenheit=[]
for i in range(5):
    temp=float(input(f'enter the temparature {i+1} in F: '))
    farenheit.append(temp)
celcius=[(j-32)*5/9 for j in farenheit]
print('list of T in F:',farenheit)
print('list of T in C:',celcius)

print('----------------------------------------')
#11
sub=['CS1101','CH2201','CS3201','CS3202','LS2201']
marks=[]
for i in range(len(sub)):
    num=float(input(f'enter the marks of {sub[i]} : '))
    marks.append(num)
marks=tuple(marks)
print('marks in 5 courses:',marks)

marks=list(marks)
for j in range(len(marks)):
    if marks[j]<50:
        marks[j]+=5
marks=tuple(marks)
print('updated marks in 5 courses:',marks)

print('----------------------------------------')
print('----------------------------------------')
