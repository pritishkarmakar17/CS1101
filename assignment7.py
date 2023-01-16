'''
ASSIGNMENT VII
PRITISH KARMAKAR
'''
import math as m



print('---------------------------------')

#q1

a=[1,2,3,4]
while True:
    print('''====CALCULATOR====
1 - Addition
2 - Subtraction
3 - Multiply
4 - Division
Any other number to exit''')
    i=int(input('Enter your choice: '))
    if i in a:
        print('Enter the two operands')
        c=float(input('Enter 1st operand: '))
        b=float(input('Enter 2nd operand: '))
        if i==1:
            print('Result=\n',c+b,sep='')
        elif i==2:
            print('Result=\n',c-b,sep='')
        elif i==3:
            print('Result=\n',c*b,sep='')
        elif i==4:
            print('Result=\n',c/b,sep='')
    else:
        print('Exiting...')
        break

print('---------------------------------')

#q2

str_ip=str(input('enter initial point (space separated): '))
str_fp=str(input('enter final point (space separated): '))
ip=[float(i) for i in str_ip.split()]
fp=[float(i) for i in str_fp.split()]
print('The distance between them:',round(m.sqrt((fp[0]-ip[0])**2+(fp[1]-ip[1])**2),2))

print('---------------------------------')

#q3
str_wld=str(input('Enter number of wins, loose, draw (space separated): '))
wld=[float(i) for i in str_wld.split()]
print('The point of the team in UCL is:',int(wld[0]*2+wld[1]*0+wld[2]*1))

print('---------------------------------')

#q4

while True:
    D=str(input('DNA sequence:\n'))
    if all([(i in ['A','T','G','C']) for i in set(D)]):
        break
    else:
        print('error-invalid DNA sequence')
        continue
R=D.replace('T','U')
print('RNA sequence:\n'+R)

print('---------------------------------')

#q5

while True:
    str_D=str(input('DNA sequence:\n'))
    if all([(i in ['A','T','G','C']) for i in set(str_D)]):
        break
    else:
        print('error-invalid DNA sequence')
        continue
nA=0
nT=0
nG=0
nC=0
lt=list(str_D)
for i in range(len(lt)):
    if lt[i]=='A':
        nA+=1
    elif lt[i]=='C':
        nC+=1
    elif lt[i]=='G':
        nG+=1
    elif lt[i]=='T':
        nT+=1
print('no. of nucleotide:\n',f'A:{nA} C:{nC} G:{nG} T:{nT}')

print('---------------------------------')

#q6

s=str(input('enter a  sequence of whitespace-separated words:\n'))
lt=list(set(s.split()))
lt.sort()
print(' '.join(lt))

print('---------------------------------')

#q7

lst = ['I','think','therefore','I', 'am','said','Rene','Descartes']
dct = {'Rene' : 0, 'Descartes' : 1, 'I' : 2, 'think': 3}

K=str(input('enter the key: '))
if (K in lst) and (K in dct):
    print(f'Value of {K} in dictionary is', dct[K])
else:
    print(f'{K} isn\'t found in either list or dictionary')


print('---------------------------------')
print('---------------------------------')








