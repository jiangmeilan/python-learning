#rescue xiaoha
b = []
with open('map.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip().split()
        new_items = map(int, items)
        b.append(new_items)

que = [[0, 0, 0, 0] for i in range(100)]
book = [[0, 0, 0, 0] for i in range(5)]
aspect = [(0, 1), (1, 0), (0, -1), (-1, 0)]
target = (2, 3)

width = len(b[0])
height = len(b)

head = 0
tail = 0
step = 0
que[tail][0] = 0
que[tail][1] = 0
que[tail][2] = 0
que[tail][3] = -1
tail += 1
book[0][0] = 1
flag = False
while head < tail:
    cur = que[head]
    father = head
    head += 1
    for k in aspect:
        tx = cur[0] + k[0]
        ty = cur[1] + k[1]
        if tx < 0 or tx >= width or ty < 0 or ty >= height: continue
        if book[ty][tx] == 0 and b[ty][tx] == 0:
            book[ty][tx] = 1
            que[tail][0] = tx
            que[tail][1] = ty
            que[tail][2] = cur[2] + 1
            que[tail][3] = father
            tail += 1
        if tx == target[0] and ty == target[1]:
            flag = True
            break
    if flag: break
print que[tail-1][2]

idx = tail - 1
trace = []
while True:
    trace.append(que[idx][:2])
    idx = que[idx][3]
    if idx == -1: break

trace.reverse()
print(trace)

#bomb person
bomb_map = []
with open('bomb_map.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        bomb_map.append(item)

row = len(bomb_map)
col = len(bomb_map[0])

que = [[0, 0] for i in range(100)]
book = [[0] * 13 for i in range(13)]
aspect = [(1, 0), (0, 1), (-1, 0), (0, -1)]

head = 0
tail = 0
start_x = 3
start_y = 3
que[tail][0] = start_x
que[tail][1] = start_y
tail += 1
book[3][3] = 1
map_g = 0


def forward(m, x, y, dx, dy):
    s = 0
    while m[y][x] != '#':
        x += dx
        y+= dy
        if m[y][x] == 'G':
            s += 1
    return s
def dfs(x, y):
    sm = 0
    sm += forward(bomb_map, x, y, -1, 0) 
    sm += forward(bomb_map, x, y, 1, 0) 
    sm += forward(bomb_map, x, y, 0, 1) 
    sm += forward(bomb_map, x, y, 0, -1) 
    global map_g, target_x, target_y
    if sm > map_g:
        map_g = sm
        target_x = x
        target_y = y
    for k in aspect:
        tx = x + k[0]
        ty = y + k[1]
        if tx < 0 or tx >= col or ty < 0 or tx >= row:continue
        if book[ty][tx] == 0 and bomb_map[ty][tx] == '.':
            book[ty][tx] = 1
            dfs(tx, ty)
    return 
dfs(3, 3)
print map_g, target_x, target_y
#
while head < tail:
    cur = que[head]
    head += 1
    for k in aspect:
        tx = cur[0] + k[0]
        ty = cur[1] + k[1]
        if tx < 0 or tx >= col or ty < 0 or tx >= row:continue
        if book[ty][tx] == 0:
            book[ty][tx] = 1
            if bomb_map[ty][tx] == '.':
                que[tail][0] = tx
                que[tail][1] = ty
                tail += 1
                sum_g = 0
                x = tx
                y = ty
                while bomb_map[y][x] != '#':
                    y += 1
                    if bomb_map[y][x] == 'G':
                        sum_g += 1
                x = tx
                y = ty
                while bomb_map[y][x] != '#':
                    y -= 1
                    if bomb_map[y][x] == 'G':
                        sum_g += 1
                x = tx
                y = ty
                while bomb_map[y][x] != '#':
                    x += 1
                    if bomb_map[y][x] == 'G':
                        sum_g += 1
                x = tx
                y = ty
                while bomb_map[y][x] != '#':
                    x -= 1
                    if bomb_map[y][x] == 'G':
                        sum_g += 1
                if sum_g > map_g:
                    map_g = sum_g
                    target_x = tx
                    target_y = ty

print map_g, target_x, target_y

#
max_g = 0
for i in range(row):
    for j in range(col):
        if bomb_map[i][j] == '.':
            sum_g = 0
            y = i
            x = j
            while bomb_map[y][x] != '#': 
                y += 1
                if bomb_map[y][x] == 'G':
                    sum_g += 1
            y = i
            x = j
            while bomb_map[y][x] != '#': 
                y -= 1
                if bomb_map[y][x] == 'G':
                    sum_g += 1
            y = i
            x = j
            while bomb_map[y][x] != '#': 
                x += 1
                if bomb_map[y][x] == 'G':
                    sum_g += 1
            y = i
            x = j
            while bomb_map[y][x] != '#': 
                x -= 1
                if bomb_map[y][x] == 'G':
                    sum_g += 1
            if sum_g > max_g:
                max_g = sum_g
                target_y = i
                target_x = j

print max_g, target_x, target_y

#

space = []
max_g = 0
for i, s in enumerate(bomb_map):
    for j, x in enumerate(s): 
        if x == '.':
            space.append([j, i])

for i in space:
    s = 0
    s += forward(bomb_map, i[0], i[1], -1, 0) 
    s += forward(bomb_map, i[0], i[1], 1, 0) 
    s += forward(bomb_map, i[0], i[1], 0, 1) 
    s += forward(bomb_map, i[0], i[1], 0, -1) 
    if s > max_g:
        max_g = s
        target = i
print max_g, target

#Adventrue Island
altitude = []
with open('high.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        altitude.append(item)


width = len(altitude[0])
height = len(altitude)
que = [[0, 0] for i in range(100)]
book = [[0] * width for i in range(height)]

located = (5, 7)
head = 0
tail = 0
que[tail][0] = located[0]
que[tail][1] = located[1]
book[located[1]][located[0]] = 1
tail += 1

while head < tail:
    for k in aspect:
        tx = que[head][0] + k[0]
        ty = que[head][1] + k[1]
        if tx < 0 or tx >= width or ty < 0 or ty >= height:continue
        if book[ty][tx] == 0 and altitude[ty][tx] != '0':
            book[ty][tx] = 1
            que[tail][0] = tx
            que[tail][1] = ty
            tail += 1
    head += 1

print 'area = %s' % tail

#
def dfs_island(x, y):
    for k in aspect:
        tx = x + k[0]
        ty = y + k[1]
        if tx < 0 or tx >= width or ty < 0 or ty >= height:continue
        if book[ty][tx] == 0 and altitude[ty][tx] != '0':
            global s
            s += 1
            book[ty][tx] = 1
            dfs_island(tx, ty)
    return

book = [[0] * width for i in range(height)]
s = 1
book[7][5] = 1
dfs_island(5, 7)
print 'Island\'s area is %s' % s

#
altitude_1 = []
with open('high.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        altitude_1.append(items)

print altitude_1
def color_island(x, y, color):
    for k in aspect:
        tx = x + k[0]
        ty = y + k[1]
        if tx < 0 or tx >= width or ty < 0 or ty >= height:continue
        if book[ty][tx] == 0 and altitude_1[ty][tx] != 0:
            global s
            s += 1
            book[ty][tx] = 1
            altitude_1[ty][tx] = color
            color_island(tx, ty, color)
    return

book = [[0] * width for i in range(height)]
s = 1
book[7][5] = 1
altitude_1[7][5] = -1
color_island(5, 7, -1)
from pprint import *
pprint(altitude_1)
print 'Island\'s area is %s' % s
        
#
def color_island_1(x, y, color):
    for k in aspect:
        tx = x + k[0]
        ty = y + k[1]
        if tx < 0 or tx >= width or ty < 0 or ty >= height:continue
        if book[ty][tx] == 0 and altitude_2[ty][tx] != 0:
            global s
            s += 1
            book[ty][tx] = 1
            altitude_2[ty][tx] = color
            color_island_1(tx, ty, color)
    return
altitude_2 = []
with open('high.txt', 'r') as f:
    for line in f.readlines():
        item = line.split()
        items = map(int, item)
        altitude_2.append(items)

book = [[0] * 10 for i in range(10)]
island_is = []
num = 0
for i, x in enumerate(altitude_2):
    for j, z in enumerate(x): 
        if z > 0:
            s = 0
            num += 1
            color_island_1(j, i, -num)
            island_is.append(s)

island_area = []
for i in island_is:
    if i > 0:
        island_area.append(i)
print num, island_area
pprint (altitude_2)
        


#plumber game
def splice_tube(x, y, front):
    global flag, top, width, height
    if x == width  and y == height - 1:
        flag = 1
        for i in range(0, top):
            print '(%d, %d)' % (que[i][0], que[i][1])
        print '-------------'
        return
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    if book[y][x] == 1:
        return
    book[y][x] = 1
    que[top][0] = x
    que[top][1] = y
    top += 1
    if tube_pattern[y][x] == 5 or tube_pattern[y][x] == 6:
        if front == 1:
            splice_tube(x + 1, y, 1)
        if front == 2:
            splice_tube(x, y + 1, 2)
        if front == 3:
            splice_tube(x - 1, y, 3)
        if front == 4:
            splice_tube(x, y - 1, 4)
    if tube_pattern[y][x] >= 1 and tube_pattern[y][x] <= 4:
        if front == 1:
            splice_tube(x, y + 1, 2)
            splice_tube(x, y - 1, 4)
        if front == 2:
            splice_tube(x + 1, y, 1)
            splice_tube(x - 1, y, 3)
        if front == 3:
            splice_tube(x, y - 1, 4)
            splice_tube(x, y + 1, 2)
        if front == 4:
            splice_tube(x + 1, y, 1)
            splice_tube(x - 1, y, 3)
    book[y][x] = 0
    top -= 1
    return

tube_pattern = []
with open('tube_pattern.txt', 'r') as f:
    for line in f.readlines():
        item = line.strip().split()
        items = map(int, item)
        tube_pattern.append(items)
        
width = 4
height = 5
book = [[0] * 4 for i in range(5)]
que = [[0, 0] for i in range(100)]
flag = 0
top = 0
splice_tube(0, 0, 1)
if flag == 0:
    print 'impossible'
else:
    print 'found'
