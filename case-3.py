# -*- coding -*- UTF-8
#case 29
def five_int(x):
    try:
        isinstance(x,int) == True
        str_five = str(x)
        n = len(str_five)
        start = n
        end = 0
        step = -1
        array = range(start,end,step)
        for i in array:
            print i
        print n
    except Exception as e:
        print('Error:',e)
five_int(12345)
five_int('string')
#case 30
def Palindrome_number(x):
    regular = 5
    if not isinstance(x,int):
        print 'x must be a int!'
        return
    string = str(x)
    if len(string) != regular:
        print 'x\'s longer must be 5'
        return
    if string[0] == string[-1] and string[1] == string[-2]:
        print 'x is a Palindrome_number.'
    else:
        print 'x is not a Palindrome_number.'
Palindrome_number(1234)
Palindrome_number('112')
Palindrome_number(12321)
def Palindrome_number_1(x):
    size = 5
    assert isinstance(x,int)
    string = str(x)
    assert len(string) == size
    if string[0] == string[-1] and string[1] == string[-2]:
        print 'x is a Palindrome_number.'
    else:
        print 'x is not a Palindrome_number.'
Palindrome_number_1(12345)
#case 31
def xxx():
    lst = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    s = raw_input('please input the first letter:').lower()
    count = 0
    lst1 = []
    for i in lst:
        if i[0] == s:
            count += 1
            lst1.append(i)
    if count == 1:
        print 'Today is %s' % lst1[0]
    else:
        s1=raw_input('please input the second letter:').lower()
        for i in lst1:
            if i[1] == s1:
                print 'Today is %s' % i
#case 32
def reverse_order(lst):
    print lst[-1::-1]
reverse_order(['s',1,2,'o'])
#case 33
def comma_csv(lst):
    lst1 = map(str,lst)
    return ','.join(lst1)
print comma_csv(['s','d'])
print comma_csv([1,2])
#case 34
#function as paramter
def add(x,y,abs):
    return abs(x) + abs(y)
print add(-1,-9,abs)
#map
print map(str,(1,2,3,4))
#reduce
print reduce(lambda x,y:x + y,(1,2,3,4))
#anonymous function
print map(lambda x:x*x,[1,2,3,4,5])
print map(lambda s:s.strip(),['','  we ',' h  h '])
#filter
print filter(lambda s: s and s.strip(),['','  ss ','asd','d f'])
#return function
def a_b():
    def c_d():
        return 1
    return c_d
print a_b()
print a_b()()
#recursion
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)
def power_1(x,n):
    if n == 0:
        return 1
    return x * power_1(x,n-1)
def reverse_letter(x):
    n = len(x)
    if n == 0:
        return 
    print x[-1]
    x = x[0:-1]
    return reverse_letter(x)
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [1, 2, 3, 4, 5, 6, 7]
print search(seq, 4, 0, 6)
print factorial(5),power_1(2,3)
reverse_letter('letter')
#case 35
#case 36
def prime_number(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        start = 2
        end = x
        array = range(start,end)
        for i in array:
            if x % i == 0:
                return False
        return True
print filter(prime_number,range(1,100))
def prime_number_1(x):
    start = 1
    end = x
    array = range(start,end)
    for num in array:
        if num > 1:
            for i in range(2,num): 
                if num % i == 0:
                    break
            else:
                print num
prime_number_1(100)
#case 37
def sort_cmp(lst):
    return sorted(lst)
print sort_cmp([1,3,2,5,9,0])

