'''
ASSIGNMENT VIII
PRITISH KARMAKAR
'''
import math


#1
while True:
    rna=str(input('RNA sequence: '))
    if len(rna)%3==0:
        break
    else:
        print('error- numbers of nucleotides is not multiple of 3')
        continue
codon=[]
for i in range(0,len(rna),3):
    codon.append(rna[i:i+3])
print('Codons are:',codon)

N='AUGC'
All=[]
for i in range(len(N)):
    for j in range(len(N)):
        for k in range(len(N)):
            All.append(N[i]+N[j]+N[k])
for p in range(len(All)):
    n=0
    for i in range(len(codon)):
        if codon[i]==All[p]:
            n+=1
    print(f'freq_{All[p]} = {n}/{len(codon)} = {round(n/len(codon),3)}')

print('------------------------------------')

#2

while True:
    rna=str(input('RNA sequence: '))
    if len(rna)%3==0:
        break
    else:
        print('numbers of nucleotides is not multiple of 3')
        continue
codon=[]
for i in range(0,len(rna),3):
    codon.append(rna[i:i+3])
#print(codon)
dct={
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
stop=['UAA','UGA','UAG']

amino=[]
for i in codon:
    if i in stop:
        break
    amino.append(dct[i.replace('U','T')])
print('Amino acid chain:',''.join(amino))

print('------------------------------------')

#3

r=float(input('input the radius of the sphere: '))
v=(4/3)*math.pi*r**3
for k in range(1,5):
    print(f'volume corrected upto %i decimal place: %.{k}f'%(k,v))

print('------------------------------------')

#4

try:
    r=float(input('input a number: '))
    if r<0:
        raise Exception
except Exception:
    print(f'Input number ({r}) is negative, have no square-root')
else:
    print('the square-root is %.3f'%math.sqrt(r))


print('------------------------------------')
print('------------------------------------')
























