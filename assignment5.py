'''
pritish karmakar

assignment v
'''
print('----------------------------------------')

import math as m

#q1

a=int(input('enter a intiger: '))
b=int(input('enter a intiger: '))
l1=[a,b]
l1.sort()
l2=list(range(l1[0],l1[1]+1))
l3=[] #list of non prime numbers
for i in l2:
    for j in range(2,i):
        if i%j==0:
            l3.append(i)
            break
for k in l3:
    l2.remove(k)
if 0 in l2:
    l2.remove(0)
print(f'prime numbers in between {l1[0]} and {l1[1]}:\n',l2)

print('----------------------------------------')

#q2

l4=[1]
while True:
    l4.append(l4[-1]*m.pi/(len(l4)))
    if abs(sum(l4)-m.exp(m.pi))<=10**(-4):
        break
print('number of terms    :',len(l4))
print('computed value     :',sum(l4))
print('actual value        :',m.exp(m.pi))
print('absolute difference:',abs(sum(l4)-m.exp(m.pi)))


print('----------------------------------------')

#q3

l5=[]
i=0
x=m.pi/2
while True:
    l5.append(((-1)**i)*((m.pi/2)**(2*i+1))/m.factorial(2*i+1))
    if (abs(sum(l5)-m.sin(m.pi/2))<=10**(-4)):
        break
    i+=1
print('number of terms    :',len(l5))
print('computed value     :',sum(l5))
print('actual value        :',m.sin(m.pi/2))
print('absolute difference:',abs(sum(l5)-m.sin(m.pi/2)))

print('----------------------------------------')

#q4

x='A'
y=' '
h=10
for i in range(1,h+1):
    print(y*(h-i)+x*(2*i))


print('----------------------------------------')

#q5

def triangle(lt): #list [x,y,z] as argument 
    s=True
    for i in range(len(l6)):
        s = s & (lt[i]<(sum(l6)-lt[i]))
    return s

l6=[]
for i in range(3):
        x=float(input(f'enter number {i+1} : '))
        l6.append(x)

if triangle(l6)==True:
    print('triangle is possible')
else:
    print('triangle is not possible')

print('----------------------------------------')

#q6

def f(x,n):
    l7=[]
    for i in range(n):
        l7.append(((-1)**i)*(x**(2*i+1))/(2*i+1))
    return sum(l7)

lt=[]
i=0
x=1/m.sqrt(3)
while True:
    i+=1
    lt.append(f(x,i))
    if (abs(6*(lt[-1])-m.pi)<=10**(-3)):
        break
print('number of terms    :',i)
print('computed value     :',6*lt[-1])
print('actual value        :',m.pi)
print('absolute difference:',abs(6*(lt[-1])-m.pi))


print('----------------------------------------')

#7

def f1(x):
    return x**(0.9)
x=10
l9=[]
while True:
    y=f1(x)
    l9.append(y)
    if y<2:
        break
    x=f1(x)
print('iteration needed:',len(l9))

print('----------------------------------------')
print('----------------------------------------')





















