e = []
with open('picture.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        e.append(items)

book = [0] * 5
n = 5
s = 0
def dfs(cur):
    global s, n
    print '%d' % cur
    s += 1
    if s == n:
        print '-------------'
        return
    for i in range(n):
        if e[cur][i] == 1 and book[i] == 0:
            book[i] = 1
            dfs(i)
    return

book[0] = 1
dfs(0)

#
b = []
with open('picture.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        b.append(items)

head = 0
tail = 0
que = [0] * 100
book = [0] * 5
que[tail] = 0
tail += 1
book[0] = 1

while head < tail:
    cur = que[head]
    for i in range(5):
        if b[cur][i] == 1 and book[i] == 0:
            que[tail] = i
            tail += 1
            book[i] = 1
        if tail >= n:break
    head += 1
for i in range(5):
    print que[i]

print '---------------'
#
c = []
with open('road.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        c.append(items)

def dfsroad(cur, s):
    global minstep
    route.append(cur)
    #if s > minstep:return
    if cur == n:
        xxx = route[:]
        lst.append(xxx)
        if s < minstep:
            minstep = s
        return
    for i in range(5):
        if c[cur][i] > 0 and book[i] == 0:
            book[i] = 1
            dfsroad(i, s + c[cur][i])
            book[i] = 0
            route.pop()
    return

lst = []
route = []
book = [0] * 5
minstep = 999
n = 4
book[0] = 1
dfsroad(0, 0)
print minstep, '\n'
print lst

print '-----------'

#
d = []
with open('traffic.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        d.append(items)

n = 4
flag = 0
book = [0] * 5
que = [[0, 0] for i in range(1000)]
head = 0
tail = 0
que[tail][0] = 0
que[tail][1] = 0
tail += 1
book[0] = 1

while head < tail:
    cur = que[head][0]
    for j in range(5):
        if d[cur][j] == 1 and book[j] == 0:
            que[tail][0] = j
            que[tail][1] = que[head][1] + 1
            book[j] = 1
            tail += 1
            if j == n:
                break
    head += 1

print que[tail - 1][1] 


#most route
e = []
with open('folyd warshall.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        e.append(items)

for k in range(4):
    for i in range(4):
        for j in range(4):
            if e[i][j] > e[i][k] + e[k][j]:
                e[i][j] = e[i][k] + e[k][j]

for i in e:
    print i


#
ai = []
with open('dijkstra.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        ai.append(items)

n = 6
dis = [0 for i in range(n)]
book = [0 for i in range(n)]
for i in range(n):
    dis[i] = ai[0][i]

book[0] = 1
inf = 999

for i in range(n - 1):
    mins = inf
    for j in range(n):
        if book[j] == 0 and dis[j] < mins:
            mins = dis[j]
            u = j
    book[u] = 1
    for v in range(n):
        if ai[u][v] < inf:
            if dis[v] > dis[u] + ai[u][v]:
                dis[v] = dis[u] + ai[u][v]

for i in range(n):
    print dis[i]

