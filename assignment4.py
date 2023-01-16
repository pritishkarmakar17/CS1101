# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:13:06 2022

@author: Pritish
ASSIGNMENT IV
"""

#1
lt=[0,10,[20,30],40,50,[60,70,80,],[90,100,110,120]]
lt1=[]
for i in lt:
    if type(i)==list:
        lt1+=i
    else:
        lt1.append(i)
print('updated list:',lt1)
    
print('----------------------------------------')

#2
R=int(input('enter no of rows   : '))
C=int(input('enter no of columns: '))
l1=[]
for r in range(R):
    l2=[]
    for c in range(C):
        while True:
            i=int(input(f'enter element at row: {r+1}, column: {c+1}: '))
            if i in range(-999,999):
                l2.append(i)
                break
            else:
                print('invalid input')
                continue
    l1.append(l2)
print('required list:',l1)
print(f'required matrix of {r+1} * {c+1}: ')
for j in l1:
    print(j)

print('----------------------------------------')

#3
L1=[3,7,13,9,7,5,13,17,23,17,7,29]
L2=['A','E','E','O','A']
def update_lt(lt):
    new_lt=[]
    for i in lt:
        if i not in new_lt:
            new_lt.append(i)
    return new_lt
print('updated list for L1:',update_lt(L1))
print('updated list for L2:',update_lt(L2))

print('----------------------------------------')

#4

#4.1
l3=[]
while True:
    k=int(input('enter a non-zero intiger: '))
    if k==0:
        break
    else:
        l3.append(k)
print('your list is:',l3)

#4.2
print('the avg of the numbers:',sum(l3)/len(l3))

print('----------------------------------------')

#5

#5.1
numbers=list(range(1,101))

#5.2
squares=[]
for i in numbers:
    squares.append(i)
    squares.append(i**2)
print('numbers=',numbers)
print('squares=',squares)

print('----------------------------------------')

#6
squares={1:1,2:4,3:9,4:16,5:25}
print('given list=',squares)
for i in range(6,10):
    squares[i]=i**2
print('modified list:',squares)
squares_keys=list(squares.keys())
print('modified list 2:',{i:squares[i] for i in squares_keys[1:]})
print('value associated with the removed key:',squares[squares_keys[0]])

print('----------------------------------------')

#7
l4=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
new_l4=[]
for i in l4:
    i.pop()
    new_l4.append(i)
print('modified array list:',new_l4)

print('----------------------------------------')

#8
D1={'a':100, 'b':200, 'c':300}
D2={'x':25,'y':18,'z':45}
def sum_values(dt):
    dt_values=[dt[i] for i in dt.keys()]
    return sum(dt_values)
print('sum of all values of D1:',sum_values(D1))
print('sum of all values of D2:',sum_values(D2))

print('----------------------------------------')

#9
t_o_t=(('jan','feb','mar','apr','may','jun','jul'),('sun','mon','tue','wed','thu','fri','sat'))
print('for april;',t_o_t[0][3])
print('for friday;',t_o_t[1][-2])
print('items: ',t_o_t[0][0],',', t_o_t[1],sep='')

print('----------------------------------------')

#10
d3={}
lst=[2,3,5,6,7,8]
for i in range(len(lst)):
    d3[lst[i]]=lst[i+2]
    if d3[lst[i]]==lst[-1]:
        break
print('required dictionary: ',d3)
    
print('----------------------------------------')
print('----------------------------------------')
























