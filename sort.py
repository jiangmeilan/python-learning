import random
#1sort merge
def merge(a, b):
    a_i = 0
    b_i = 0
    c = []
    while a_i < len(a) and b_i < len(b):
        if a[a_i] < b[b_i]:
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1
    if a_i < len(a):c += a[a_i:]
    if b_i < len(b):c += b[b_i:]
    return c
a = [1, 3, 5, 6]
b = [2, 4, 7, 8, 9]
print merge(a, b)
def sort_merge(x):
    if len(x) <= 1: return x
    a = sort_merge(x[: len(x) / 2])
    b = sort_merge(x[len(x) / 2:])
    return merge(a, b)
print sort_merge([1, 4, 6, 2, 9, 0, 8])

#2sort swap
def sort_swap(lst):
    N = len(lst)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print sort_swap([random.randint(1, 100) for i in range(20)])

#3sort bubble
def sort_bubble(lst):
    N = len(lst) - 1
    for j in range(len(lst) - 1):
        for i in range(N - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        N = N - 1
    return lst
print sort_bubble([random.randint(1, 100) for i in range(20)])

#4sort insert
def sort_insert(lst):
    lst1 = [lst[0]]
    if lst[1] >= lst[0]:
        lst1.append(lst[1])
    else:
        lst1.insert(0, lst[1])
    for i in range(2, len(lst)): 
        if lst[i] >= lst1[i - 1]:
            lst1.append(lst[i])
        else:
            if lst[i] <= lst1[0]:
                lst1.insert(0, lst[i])
            else:
                for j in range(len(lst1) - 1):
                    if lst[i] > lst1[j] and lst[i] < lst1[j + 1]:
                        lst1.insert(j + 1, lst[i])
                        break
                    elif lst[i] == lst1[j]:
                        lst1.insert(j + 1, lst[i])
                        break
    return lst1
print sort_insert([random.randint(1, 100) for i in range(20)])

print('-------------------------------')
def sort__insert(lst):
    sort_lst = []
    for x in lst:
        for i in range(len(sort_lst)):
            if x < sort_lst[i]: 
                sort_lst.insert(i, x)
                break
        else:
            sort_lst.append(x)
    return sort_lst


lst = [random.randint(1, 10) for x in range(20)]
print(sort__insert(lst))
print ('------------------')
#5sort radix
def radix_sort(lst):
    lst1 = [0 for i in range(10)]
    for x in lst:
        lst1[x] += 1
    #for i in range(len(lst1)):
    for i, x in enumerate(lst1):
        for j in range(x):
            print i
radix_sort([random.randint(1, 9) for i in range(10)])

print ('------------------')

f = lambda x, y: (x > y) * x + (y > x) * y
print f(6, 8)
print False * 4
print True * 4

#6quick sort
def quick_sort(lst, left, right):
    if left >= right:
        return lst
    key = lst[left]
    low = left
    high = right
    while left < right:
        while left < right and lst[right] >= key: 
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= key:
            left += 1
        lst[right] = lst[left]
    lst[right] = key
    quick_sort(lst, low, left - 1)
    quick_sort(lst, left + 1, high)
    return lst
print quick_sort([random.randint(1, 10) for i in range(20)], 0, 19)
def quick_sort(lst, left, right):
    if left >= right:
        return lst
    key = lst[left]
    low = left
    high = right
    while left < right:
        while left < right and lst[right] >= key:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= key:
            left +=1
        lst[right] = lst[left]
    lst[right] = key
    quick_sort(lst, low, left - 1)
    quick_sort(lst, left + 1, high)
    return lst
print quick_sort([random.randint(1, 10) for i in range(20)], 0, 19)

#heap sort
def adjust_heap(lst, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lst[lchild] >lst[max]:
            max = lchild
        if rchild < size and lst[rchild] > lst[max]:
            max = rchild
        if max != i:
            lst[i], lst[max] = lst[max], lst[i]
            adjust_heap(lst, max, size)

def build_heap(lst, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lst, i, size)

def heap_sort(lst):
    size = len(lst)
    build_heap(lst, size)
    for i in range(0, size)[::-1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)
    return lst
print heap_sort([random.randint(1, 10) for i in range(20)])

#xiaohengmaishu
def unique_sort(lst):
    lst2 = []
    lst1 = [0 for i in range(10)]
    for x in lst:
        lst1[x] += 1
    for i, x in enumerate(lst1):
        if x >= 1:
            lst2.append(i)
    return lst2   
def unique_sort1(lst):
    lst1 = sort_bubble(lst)
    lst2 = [lst1[0]]
    for i in range(1, len(lst1)):
        if lst1[i] != lst1[i - 1]:
            lst2.append(lst1[i])
    return lst2   
lst = [random.randint(0, 9) for i in range(20)] 
print unique_sort(lst)
print unique_sort1(lst)
print heap_sort(lst)
