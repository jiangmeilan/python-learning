# -*- coding: UTF-8 -*-
#case 1

def case1() :
    n = 0
    count = 0
    start = 1
    end = 5
    array = range(start, end)
    for i in array:
        for j in array:
            for k in array:
                if (i != j) and (i != k) and (j != k):
                    n = n + 1
                    print i, j, k
    print n
    print set([1,1,2,3,4,4])

case1()

#case 2 (运算符使用错误)
'''j = 0
i =int(raw_input('输入当月利润：'))
if i > 100:
    j = 10*10% + 10*7.5% + 20*5% + 20*3% + 40*1.5% + (i-100)*1%
elif i > 60:
    j = 10 * 10% + 10 * 7.5% + 20 * 5% + 20 * 3% + (i-60) * 1.5%
elif i > 40:
    j = 10*10% + 10*7.5% + 20*5% + (i-40)*3%
elif i > 20:
    j = 10*10% + 10*7.5% + (i-20)*5% 
elif i > 10:
    j = 10*10% + (i-10)*7.5%  
else:
    j = i*10%
print j'''
#case 2
'''try:
    j=0.0  
    i=int(raw_input('please input:'))
except Exception as e:
    print('Error:',e)
else:
    if i>100:
        j=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(i-100)*0.01
    elif i>60:
        j=10*0.1+10*0.075+20*0.05+20*0.03+(i-60)*0.015
    elif i>40:
        j=10*0.1+10*0.075+20*0.05+(i-40)*0.03
    elif i>20:
        j=10*0.1+10*0.075+(i-20)*0.05
    elif i>10:
        j=10*0.1+(i-10)*0.075
    elif i>0:
        j=i*0.01
    else:
        print('Error:i must be >= 0')
    print j
print int(-10.1)
print int('0xa',16)
print int('17',8)
a = raw_input('str or int:')
print type(a)'''
#case 3
import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x*x==i+100) and (y*y==i+268):
        print i
#case 4
'''l1 = [31,29,31,30,31,30,31,31,30,31,30,31]
l2 = [31,28,31,30,31,30,31,31,30,31,30,31]
d = 0
x=int(raw_input('which year:'))
y=int(raw_input('which month:'))
z=int(raw_input('which day:'))
if y == 1:
    d = z
if y == 2:
    d = 31 + z
if y > 2:
    if x % 100 == 0:
        if x % 400 == 0: 
            for i in l1[:y-1]:
                d += i
            d = d + z
        else:
            for i in l2[:y-1]:
                d += i
            d = d + z
    else:
        if x % 4 == 0:
            for i in l1[:y-1]:
                d += i
            d = d + z
        else:
            for i in l2[:y-1]:
                d += i
            d = d + z
print 'It is %dth day' % d'''
#case 5 
'''x = int(raw_input('int:'))
y = int(raw_input('int:'))
z = int(raw_input('int:'))
print sorted([x,y,z])
def reversed_cmp(x,y):
    if x < y:
        return 1
    if x > y:
        return -1
    if x == y:
        return 0
print sorted([x,y,z],reversed_cmp)
def cmp_ignore(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    if u1 == u2:
        return 0
print sorted(['adf','whjhhh','zhjf','Ahf'],cmp_ignore)'''
#case 6
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print fib(10)
#case 7(需修改)
'''l1 = raw_input('input a list:')
l2 = []
for i in range(len(l1)):
    l2.append(l1[i])
print l2'''
#case 7
a=[1,2,3,4]
b=a[:2]
c=a[:]
d=a[2::2]
print b,c,d
#case 8
for i in range(1,10):
    for j in range(1,10):
        #print str(i),'*',str(j),'=',i*j
        print '%d * %d = %d' %(i,j,i*j)
#case 9(多练习)
import time
myD = {1:'a',2:'b'}
for key,value in dict.items(myD):
    print key,value
    time.sleep(1)
#case 10(多练习)
import time
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#case(词频排序)
import re
import collections
with open('xiaowangzi.txt','r') as f:
    words=f.read()
    words=re.sub('!|\"|,|\.|\d|()','',words)
    words=words.split()
    result={}
    for word in words:
        if word not in result:
            result[word]=0
        result[word]+=1
    d=collections.OrderedDict(sorted(result.items(),key=lambda t:-t[1]))
    n=0
    for key,value in d.items():
        print key + ':%d' % value
        n+=1
        if n == 10:
            break
