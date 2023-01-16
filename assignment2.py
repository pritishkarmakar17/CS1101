# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:18:10 2022

@author: Pritish

ASSIGNMENT 2
"""

#1
x='Pritish Karmakar'
for i in range(1,16):
    print(i,x)

print('----------------------------')
#2
for i in list(range(1,16)):
    if i%3==0:
        print(i,x)   
    
print('----------------------------')    
#3
str1='abcdefghijkl'
for i in range(len(str1)):
    print(str1[i:]) 
    
print('----------------------------')
#4
l1=[0,3,1,2,8,9,0,4,7]
m1=l1[0]
for i in range(len(l1)):
    if l1[i]>m1:
        m1=l1[i]
print('maximum value:',m1)

l2=[0,-1,-3,-4,3,8,9,11,-2]
m2=l2[0]
for i in range(len(l2)):
    if l2[i]>m2:
       m2=l2[i]
print('maximum value:',m2)

print('----------------------------')       

#5
l1=[0,3,1,2,8,9,0,4,7]
l2=[0,-1,-3,-4,3,8,9,11,-2]
m3=l1[0]
n3=l1[0]
for i in range(len(l1)):
    if l1[i]>m3:
        m3=l1[i]
    if n3>l1[i]:
        n3=l1[i]
print('maximum value for l1:',m3,'and index number:',l1.index(m3))
print('minimum value for l1:',n3,'and index number:',l1.index(n3))

m4=l2[0]
n4=l2[0]
for i in range(len(l2)):
    if l2[i]>m4:
        m4=l2[i]
    if n4>l2[i]:
        n4=l2[i]
print('maximum value for l2:',m4,'and index number:',l2.index(m4))
print('minimum value for l2:',n4,'and index number:',l2.index(n4))


print('$ maximum value for l1:',max(l1),'and index number:',l1.index(max(l1)))
print('$ minimum value for l1:',min(l1),'and index number:',l1.index(min(l1)))
print('$ maximum value for l2:',max(l2),'and index number:',l2.index(max(l2)))
print('$ minimum value for l2:',min(l2),'and index number:',l2.index(min(l2)))

print('----------------------------')
#6
lst=[]
name=str(input('enter your name: '))
lst.append(name)
yoj=str(input('year of joining: '))
lst.append(yoj[-2:])
cid=str(input('course id: '))
lst.append(cid)
sid=str(input('student id: '))
lst.append(sid)
print(lst)
print('Your IISER email id: ','-'.join(lst)+'@iiserkol.ac.in')

print('----------------------------')
#7
str1='123'
str2='234'
str3='456'
lt=[eval(str1),eval(str2),eval(str3)] 
print('sum=',sum(lt))

product=1
for a in lt:
    product*=a
print('product=',product)

print('average= ',sum(lt)/len(lt))

print('----------------------------')
#8
add=0
for i in range(5):
    n=float(input(f'enter number {i+1}: '))
    add+=n
print('total=',add)
print('----------------------------')
#9
#9.a
l4=[]
for i in range(10):
    n=float(input(f'marks of student {i+1}: '))
    l4.append(n)
print('list of the marks: ',l4)
#9.b
l4.sort(reverse=True)
print('marks in decending order: ',l4) 
#9.c
for i in range(len(l4)):
    if l4[i]<45:
        l4[i]+=5

print('new marks list: ',l4)  
#9.d
num=0
for i in range(len(l4)):
    if l4[i]<50:
        num+=1
print('no. of failure: ',num)

print('----------------------------')
#10
#10.a
l5=[]
for i in range(10):
    x=int(input(f'enter a intiger {i+1}: '))
    l5.append(x)
print('the entire list:',l5 )
#10.b
l5.sort()
print('the sorted list', l5)
#10.c
lm=[min(l5),max(l5)]
for i in range(len(lm)):
    l5.remove(lm[i])
print('updated list:', l5)



print('----------------------------')
print('----------------------------')
#1
email=str(input('enter your IISER email in format \'name-rollno@iiserkol.ac.in\': '))
print('your name:',email.split('-')[0])
print('your roll no.:',email.split('-')[1].split('@')[0])
print('----------------------------')
#2

name=str(input('Enter your full name: '))
N=name.split(' ')
A=[]
for i in range(len(N)):
    A.append(N[i][0])
    A.append('.')
print('abbreviation of your name:',''.join(A))




























    
