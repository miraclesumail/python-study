# coding=utf-8
import random
import math

class C:
    def __init__(self,count):
        self.count = count

#是计算机技术

longList = [C(random.random()) for i in xrange(10)] 

longList.sort(key = lambda c: c.count,reverse=True) 
for i in range(len(longList)):
    print(longList[i].count)

var1 = {'x':3,'s':9,'d':5}
for k,v in var1.items():
    print k,'corresponds to',v


print var1.values()        

strHello = "the length of %s is %d" %('Hello World',len('Hello World'))
print strHello

print "%10.3s" % ("jcodeer")
print "%.3s is %.5s" % ("jcodeer",'ddfffeee')
print "%02d is" % int(math.pi)
print "%09d is" % 2345

#从这里看出 range或者切片 都不包含结尾
for i in range(1,9,2):
    print "the result is %d" % i

print "减肥法减肥"   

name = raw_input() 
print "my name is %s" % name

print 17/3

def hello(num,flag):
    aa = [i**2 for i in range(num)]
    i = 2 if flag else 1
    return aa[i],aa[3]

a,b = hello(5,True)
print 'a is %d b is %d' % (a,b)

#split
str = 'www fff ggg hhh'
arr = str.split(' ',2)
print arr

squares = [1, 4, 9, 16, 25]
squares = squares + [36, 49, 64, 81, 100]
print squares

# 注意aa的类型是tuple 元祖
def add(first,*aa):
    print type(aa)
    aa = first + sum(aa)/len(aa)
    return aa

print add(2,3,4,5)

asd = (3,4,5)
print sum(asd)

# 2个**是dict
def make(aa,**qwe):
    print aa
    print type(qwe)
    str = ['%s === %s' % item for item in qwe.items()]
    ss = (' ').join(str)
    return ss

print make('ss',size = 'aaa', ddd = 'dddww')

def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict

anyargs(3,4,5,ee='dd',ff='fff')

def func1(x,y):
    return x+y

def func2(fn,arg):
    return fn(*arg)

print func2(func1,(3,4))

def call1():
    n = 3
    def call2():
        print n
        
    def get_n():
        return n

    def set_n(value):
        n = value

    call2.get_n = get_n
    call2.set_n = set_n
    
    return call2    

aa = call1()
aa()

aa.set_n(8)
print aa.get_n()

def outer():
    d = {'y' : 0}
    def inner():
        d['y'] += 1
        return d['y']
    return inner

f = outer()
print(f(), f(), f()) #prints 1 2 3

def stack():
    item = [2,3,4]

    def s():
        None

    def push(a):
        item.append(a)

    def get():
        return item    
    s.push = push
    s.get = get

    return s    

s = stack()
print s.get()
s.push(5)
print s.get()

class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.extend(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

sss = Stack2()
sss.push([2,3,4])    
print len(sss)