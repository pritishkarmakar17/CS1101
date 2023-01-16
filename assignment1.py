# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 08:44:17 2022

@author: Pritish (21MS179)
"""

#question no 1: Exploring list
#1b
x=list(range(0,10))
#1c
y=list(range(3,13)) 
#1d
print(x[::-1]) 
#1e
print('odd entries in x : ',x[1::2],',\n','even entries in x: ',x[0::2],sep=('')) 
#1f 
print(x[3]) 
print(y[0])
print('the statement is',x[3]==y[0])
#1g
print(10 in x)
#1h
print(7 in y) 
#1i
print('combined list: ',x+y) 
#1j
x.reverse()
print('new list: ',x+y) 
print('index no. of maximum number is',(x+y).index(max(x+y)))
print('index no. of minimum number is',(x+y).index(min(x+y)))
#question no 2: strings are list
#2a
x=str('The quick brown fox jumps over the lazy dog')
#2b
print('fox' in x)
#2c
print(x[::-1])
#2d
print(x[::3])
#2e
print(x[::4])
#2f
print(len(x))
#2g
print(x[::-2])
#2h
y=x[:4]
z=x[-3:]
print(y+z)
#2i
print(y*10)

#question no 3: numbers
#3a
x=1.2
#3b
y=12
#3c
z=24
#3d
print('x/y=',x/y,',','y/z=',y/z,',','z/x=',z/x)
print('types of x/y,  y/z, z/x be respectively',type(x/y),',',type(y/z),',',type(z/x))
#3e
print(3**7)
#3f
print(2.0**3)
print(8.0)
#3g
print(y+z)
print(str(y)+str(z))
print(y+z==str(y)+str(z))

#question no 4: miscellaneus
#4a
print('Hello World')
#4b
print('Hello World')#this is python programming
#4c
name=str(input('Enter your name: '))
age=str(input('Enter your age: '))
roll=str(input('Enter your roll number: '))
print('Hello! My name is ',name,'. ','I am ',age,' years old. My roll number is ',roll,'.',sep=(''))
#4d
m1=str(input('first number: '))
m2=str(input('second number: '))
print('sum of strings =',(m1+m2))
#4e
n1=int(input('first number: '))
n2=int(input('second number: '))
print('sum of intigers =',n1+n2)
#4f
print('It\'s good to learn Python')
#4g
print('The man asked, \"Where to meet you?\" I said, \"Well, use Google Meet!\"' )
#4h
v='thank you'
print('type of v is: ',type(v))
#4i
Name=str(input('Enter your name:'))
print('My name is',Name)
#4j
name=str(input('Enter your name: '))
age=str(input('Enter your age: '))
gender=str(input('Enter your gender: '))
print('Good Morning',name +'! You are a',gender,'of',age,'years.'  )



















