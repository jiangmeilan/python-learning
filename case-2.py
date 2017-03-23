# -*- coding: UTF-8 -*-
#case 10
import time
print time.strftime('%Y-%m-%d %X',time.localtime())
time.sleep(1)
print time.strftime('%Y-%m-%d %X',time.localtime())
#case 11
#case 12
def sushu(x):
    #for x in range(101,200):
        for i in range(2,x): 
            if x % i == 0:
                return False
        return True
print filter(sushu,range(101,200))
print len(filter(sushu,range(101,200)))
#case 13
for i in range(100,1000):
    x = str(i)
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if a**3 + b**3 + c**3 == i:
        print i
#case 14
def is_prime_numeber(x):
    if x==1 :
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i ==0:
                return False
        return True
def prime_factorization(x): 
    u=x
    l=[]
    for i in range(1,x):
        if not is_prime_numeber(i):continue
        while x%i==0:
            l.append(i)
            x=x/i
    #print '%u'% u + '=' + map(str,l)
    return l
print prime_factorization(90)
li=('1','2','3','4')
print '*'.join(li)
#case 15
'''a = int(raw_input('please input your score:'))
if a>=90:
    grade = 'A'
elif a>=60:
    grade = 'B'
else:
    grade = 'C'
print '%d belongs to %s'% (a,grade)
#case 16
print time.strftime('%m %d %Y',time.localtime())
#case 17
import string
s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d'%(letters,space,digit,others)
#case 18
a=raw_input('please input int:')
n=int(raw_input('please input int:'))
s=0
for i in range(1,n+1):
    x=int(a*i)
    s+=x
print s'''
#case 19
def add(x,y):
    return x+y
for i in range(1,1000):
    num=0
    if prime_factorization(i) :
        num = reduce(add,prime_factorization(i))
    if i == num:
        print '%i is perfect' % i
#case 19'
for x in range(2,1000):
    u=x
    l=[1]
    for i in range(2,x):
        if x%i ==0:
            l.append(i)
    if u == reduce(add,l):
        print u,'\n',l
        print '%u' % u + 'is perfect!'

#case 20
s=100
h=50
for x in range(2,11):
    s+=2*h
    h*=0.5
print s,h
#case 21
n=1
for i in range(1,10):
    n=(n+1)*2
print n
#case 22
team_a=['a','b','c']
team_b=['x','y','z']
for i in team_a:
    for j in team_b:
        if i=='a' and j=='x':continue
        if i=='c' and (j=='x' or j=='z'):continue
        print(i + '\t' + j)
i='c'
for j in team_b:
    if j=='x' or j=='z':continue
    cb=j
print (i,cb)
i='a'
for j in team_b:
    if j=='x' or j==cb:continue
    ab=j
print (i,ab)
i='b'
for j in team_b:
    if j==cb or j==ab:continue
    bb=j
print (i,bb)
#case 23
n=6
k=1
for i in range(1,5):
    print ' '*n + '*'*k + '\n'
    n=n-1
    k=k+2
n=n+1
k=k-2
for j in range(1,4):
    n=n+1
    k=k-2
    print ' '*n + '*'*k + '\n'
#case 24
s=0.0
a,b=0.0,1.0
d,c=1.0,1.0
for i in range(20):
    a,b=b,a+b
    d,c=c,d+c
    m=c/b
    s+=m
print s
#case 25
def jiecheng(x):
    s=0
    for i in range(1,x+1):
        w=1
        for j in range(1,i+1):
            w*=j
        s+=w
    return s
print jiecheng(20)
#case 26
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(5)
#case 27
def output(s,l):
    if l==0:
        return
    print s[l-1]
    output(s,l-1)
s=raw_input('please input a string:')
l=len(s)
output(s,l)
#case 28
def age(n):
    if n == 1:c=10
    else:c=age(n-1)+2
    return c
print age(5)
#case 29
s=raw_input('please input a int:')
l=len(s)
print('%s'%s + 'has' + '%d'%l)
print s[-1::-1]
