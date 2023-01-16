'''
assignment VI
PRITISH KARMAKAR
'''
print('----------------------------------------')

#q1

def g(n):
    lt=[i/(i+1) for i in range(1,n+1)]
    return sum(lt)

for i in range(1,21):
    print(f'g({i}) =',g(i))

print('----------------------------------------')

#q2

def factorial(x):
    n=1
    for i in range(1,x+1):
        n*=i
    return n

for i in range(1,9):
    print(f'factorial of {i} :',factorial(i))

print('----------------------------------------')

#q3

from math import log, sin, cos, pi

def trig(t):
    t_rad=t*pi/180
    return sin(2*t_rad)

for i in range(0,91,10):
    print(i,', ',trig(i),sep='')

print('----------------------------------------')

#q4
def modified_str(txt):
    lt=list(txt)
    for i in range(1,len(txt),2):
        m=lt[i]
        del lt[i]
        lt.insert((i-1),m)
    return ''.join(lt)
        


text=str(input('Enter a text: '))
print( 'the result is :',modified_str(text))

print('----------------------------------------')

#q5

s=str(input('enter a string : '))

while True:
    if ('(' not in s) & (')' not in s):
        break
    l=s.index('(')
    r=s.index(')')
    if r!=(len(s)-2):
        s=s[:l]+s[r+2:]
    else:
        s=s[:l-1]+s[r+1:]

print(s)

print('----------------------------------------')

#q6

n=int(input('enter a intiger : '))
odd=0
even=0
for i in range(n):
    while True:
        x=int(input(f'enter value {i+1} : '))
        if x<=0:
            print('invalid input')
            continue
        else:
            break
    if x%2==0:
        even+=1
    else:
        odd+=1

print('Number of even numbers :', even)
print('Number of odd numbers  :', odd)

print('----------------------------------------')

#q7

def sum_series(n):
    term=[]
    for i in range(n):
        d=0
        for j in range(i+1):
            d+=3*(10**(j))
        term.append(d)
    return sum(term)

N=int(input('enter a intiger : '))
print('the result is :',sum_series(N))

print('----------------------------------------')

#q8

from math import factorial
def fact_sum(x):
    lt=list(str(x))
    s=0
    for j in range(len(lt)):
        s+=factorial(eval(lt[j]))
    return s

strong=[]
for i in range(1,100001):
    if i==fact_sum(i):
        strong.append(i)
print('all strong numbers between 1 and 100000 :',strong)
        
print('----------------------------------------')
print('----------------------------------------')

#q9

y=int(input('enter year : '))
m=int(input('enter month : '))
d=int(input('enter date : '))
y1=1900
m1=1
d1=1

day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
M={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
M1={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

leapyear=[]
for i in range(1900,y):
    if i%4==0:
        leapyear.append(i)
    if i%100==0 and i%400!=0:
        leapyear.pop()

day_no=0
for i in range(1900,y):
    if i in leapyear:
        day_no+=366
    else:
        day_no+=365

if y in leapyear:
    day_no+= sum([M1[i] for i in range(1,m)])
else:
    day_no+= sum([M[i] for i in range(1,m)])

day_no+= d

k=day_no%7

print(f'it is a {day[k-1]}.')

print('----------------------------------------')









            














































