import random

def quick_sort(lst, left, right):
    if left >= right:
        return lst
    low = left
    high = right
    base = lst[left]
    while left < right:
        while left < right and lst[right] >= base:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= base:
            left += 1
        lst[right] = lst[left]
    lst[left] = base
    quick_sort(lst, low, left - 1)
    quick_sort(lst, left + 1, high)
    return lst
l = [random.randint(1,10) for i in range(20)]
print quick_sort(l, 0, 19)

def opt_sort(lst):
    N = len(lst)
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
l = [random.randint(1,10) for i in range(20)]
print opt_sort(l)

#jie mi qq numeber
lst = [6, 3, 1, 7, 5, 8, 9, 2, 4]
lst1 = []
while len(lst) > 1:
    lst1.append(lst[0])
    x = lst[1]
    del lst[0:2]
    lst.append(x)
lst1.append(lst[0])
print lst1

head = 0
tail = 9
l = [6, 3, 1, 7, 5, 8, 9, 2, 4]
l1 = []
while True:
    l1.append(l[head])
    head += 1
    if head >= len(l):
        break
    l.append(l[head])
    head += 1
    tail += 1
print l1

#cat fishing
def cat_fish(lst_x, lst_y):
    player = [lst_x, lst_y]
    desk = []
    while lst_x and lst_y:
        for x in player:
            _x = x.pop(0)
            if _x in desk:
                x.append(_x)
                while True:
                    del_x = desk.pop()
                    x.append(del_x)
                    if del_x == _x: break
            else:
                desk.append(_x)
            if not lst_x or not lst_y:
                break
    return player[0] if player[0] else player[1]
print cat_fish([2, 4, 1, 2, 5, 6], [3, 1, 3, 5, 6, 4])

 
#bomb person
#huo cai gun deng shi
def gun(x):
    num = 0
    f = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    while x / 10 != 0:
        num += f[x % 10]
        x = x / 10
    num += f[x]
    return num
def gun_main(m):
    sum = 0
    for a in range(111):
        for b in range(111):
            c = a + b
            if gun(a) + gun(b) + gun(c) == m -4:
                sum += 1
                print '%d + %d = %d' % (a, b, c)
    print 'yigongkeyipingchu: %s ge' % sum
gun_main(18)

#depth search
n = 5
a = [0 for i in range(n + 1)]
book = [0 for i in range(n + 1)]
def ovalall(step):
    if step == n + 1:
        print ','.join([str(a[i]) for i in range(1, n+1)])
        return
    for i in range(1, n + 1):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            ovalall(step + 1)
            book[i] = 0

ovalall(1)


n = 9
a = [0 for i in range(n + 1)]
book = [0 for i in range(n + 1)]
cnt = 0
def ovalall_1(step):
    if step == n + 1:
        if a[1] * 100 + a[2] * 10 + a[3] + a[4] * 100 + a[5] * 10 + a[6] == a[7] * 100 + a[8] * 10 + a[9]:
            global cnt
            cnt = cnt + 1
            print '%d%d%d + %d%d%d = %d%d%d' % (a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
            return
    for i in range(1, n + 1):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            ovalall_1(step + 1)
            book[i] = 0

ovalall_1(1)
print cnt

#rescue xiaoha
a = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
nxsp = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min = 999
n = 3
m = 4
p = 2
q = 3
book = [[0] * 4 for i in range(5)]
def dfs(x, y, step):
    if x == p and y == q:
        if step < min:
            global min
            min = step
        return
    for k in range(3):
        tx = x + nxsp[k][0]
        ty = y +nxsp[k][1]
        if tx < 0 or tx > n or ty < 0 or ty > m:
            continue
        if a[ty][tx] == 0 and book[ty][tx] == 0: 
            book[ty][tx] = 1
            dfs(tx, ty, step + 1)
            book[ty][tx] = 0
book[0][0] = 1
dfs(0, 0, 0)
print min

#read matrix
print('--------------------------------')
b = [] 
with open('map.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip().split(' ')
        new_line = [int(x) for x in items]
        b.append(new_line)
print(b)

