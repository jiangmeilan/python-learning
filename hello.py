# -*- coding -*- UTF-8
f=open('xiaowangzi.txt','r+')
#print f.read()
import string
letters=0
space=0
digit=0
others=0
for c in f:
    if c.isalpha():
        letters +=1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit +=1
    else:
        others +=1
print 'char=%d,space=%d,digit=%d,others=%d' %(letters,space,digit,others)
print pow(2,3)
print 2**3
print list('hello')
str='-'
s=('a','b')
print str.join(s)
l=[1,2,3,4]
del l[0]
print l
name=list('peal')
name[2:] = list('python')
name[2:2] = 1,2,3
print name
'''with open('xiaowangzi.txt','r') as f:
    data=[]
    str1=f.read(10240)
    data.append(str1)
    str2=f.read(10240)
    data.append(str2)
    str3=f.read(10240)
    data.append(str3)
    l1=str1.split()
    l2=str2.split()
    l3=str3.split()
    print l1,l2,l3,len(l1),len(l2),len(l3)
with open('xiaowangzi.txt','r') as f:
    for line in f.readlines():
        print line.strip()'''
def Fib(x):
    a,b=0,1
    for i in range(1,x+1):
        a,b=b,a+b
    return a
print Fib(8)
with open('word_rank.txt','r') as f:
    d=[]
    str=f.read()
    l=str.split()
    l1=set(l)
    for i in l1:
        sub='%s' % (i)
        d.append(str.count(sub,0,-1))
    print d,len(d)
    q=sorted(d)
    print l1
    for x in range(-1,-11,-1):
        for n in l1:
            sub1='%s' %(n)
            if str.count(sub1,0,-1) == q[x]:
                print(sub1)
'''name=''
while not name:
    name=raw_input('please input your name:')
print 'Hello,%s!' % name
from math import sqrt
for n in range(99,0,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
while True:
    word = raw_input('p:')
    if not word:
        break
    print 'word'
word = 'd'
while word:
    word = raw_input('p:')
    print 'word' 
d={'a':1,'b':2,'c':3}
d['d']=4
print d'''
import re
import collections
def count_word(path):
    result={}
    with open(path) as file_obj:
        all_the_text=file_obj.read()
        all_the_text=re.sub('\"|,|\.','',all_the_text)
        for word in all_the_text.split():
            if word not in result:
                result[word]=0
            result[word]+=1
        return result
def sort_by_count(d):
    d=collections.OrderedDict(sorted(d.items(),key=lambda t:-t[1]))
    return d
if __name__=='__main__':
    file_name='word_rank.txt'
    dword= count_word(file_name)
    dword= sort_by_count(dword)
    for key , value in dword.items():
        print key + ':%d' % value
#2048
import random
class Matrix:
    def __init__(self, width = 4, height = 4):
        self.width = width
        self.height = height
        self.status = [[0] * width for i in range(height)]

    def prepare(self, k):
        location = random.sample(range(self.width * self.height), k)
        for loc in location:
            row = loc / self.width
            col = loc % self.width
            self.status[row][col] = 2

    def next(self):
        available = []
        for r in range(self.height):
            for c in range(self.width):
                if self.status[r][c] == 0:
                    available.append((r, c))
        loc = random.sample(available, 1)[0]
        self.status[loc[0]][loc[1]] = 2
 
class Action:
    def __init__(self):
        pass
    def move(self, event, matrix):
        if event == 258:
            self.move_up(matrix)
        elif event == 259:
            self.move_down(matrix)
        elif event == 260:
            self.move_left(matrix)
        elif event == 261:
            self.move_right(matrix)

    def move_left(self, matrix):
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = item[i] if i < len(items) else 0
            for i in range(1,len(line)):
                if line[i] == line[i - 1]:
                    line[i - 1] += line[i]
                    line[i] = 0

            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = items[i] if i < len(items) else 0

    def move_right(self, matrix): 
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in len(line):
                line[-i] = items[-i] if i < len(items) + 1 else 0
            for i in len(line) -1:
                if line[i] == line[i + 1]:
                    line[i + 1] += line[i]
                    line[i] = 0
            items = filter(lambda x:x != 0, line)
            for i in range(len(line)):
                line[-i] = items[-i] if i < len(items) + 1 else 0

    def move_up(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if r < len(items) else 0
            for r in range(1, matrix.height):
                if status[r][c] == status[r - 1][c]:
                    status[r -1][c] += status[r][c]
                    status[r][c] = 0
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if i < len(items) else 0

    def move_down(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0
            for r in range(matrix.height - 1):
                if status[r][c] == status[r + 1][c]:
                    status[r + 1][c] += status[r][c]
                    status[r][c] = 0
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0



        
       

import curses
class Render:
    def __init__(self):
        pass

    def show(self, screen, matrix):
        screen.clear()
        status = matrix.status
        for line in status:
            screen.addstr(' '.join('%d' % x for x in line))
            screen.addstr('\n')

def main(stdscr):
    curses.use_default_colors()
    
    matrix = Matrix()
    action = Action()
    render = Render()
    matrix.prepare()
    render.show(stdscr, matrix)

    while True:
        key = stdscr.getch()
        if key == ord('q'):break
        action.move(key, matrix)

curses.wrapper(main)

