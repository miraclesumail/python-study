# coding=utf-8
from functools import partial

def spam(a,b,c,d):
    print a,b,c,d

s = partial(spam,1,2)
s(3,4)    

def axiba(fn,*arg):
    def ss(*aa):
        bb = arg + aa
        fn(*bb)
    return ss    

abc = axiba(spam,1,2)
abc(3,4)


add = lambda x,y: x+y
print add(2,3)

# 注意sorted之后需要一个新的对象
names = ['www dbc','eee fgh','fff alk']
names = sorted(names,key = lambda name:name.split(' ')[-1].lower())
print names

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = map(lambda x,y: x+y , list1, list2)
print list3

# 注意tuple是immutable的  list可变  可以先list(tuple) 在用list.append 

def apply_async(func, args,callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), print_result)

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()


def call(handler,*arg):
    handler.send(None)
    # next(hanler) 也可以
    for i in arg:
        for ele in i:
            handler.send(ele)


call(handler,[1,2,3],[4,5],[6,7,8])

def aaa(obj):
    qwe = (str(type(obj))).split(' ')[1]
    return qwe[0:len(qwe)-1]

# 对于闭包可以改变的事引用类型
def cnt(param):
    d = {'y' : 0}
    def aa():
        d['y'] += 1
        print 'i am',param,'number',d['y']
    return aa

asd = cnt('www')
asd()
asd()

def abc(fn):
    def aa(num):
        print fn(num)
    return aa    

@abc
def hello(cc):
    return cc**3

hello(3)

# 默认参数 第一次有效
x = 42
def asd(a,b=x):
    print a,b

asd(1)

x = 52
asd(1)   

xy = 2
def funcx():
    global xy    #跟上面函数的不同之处
    xy = 9
    print "this x is in the funcx:-->",xy

funcx()
print "--------------------------"
print "this x is out of funcx:-->",xy

def total(aa,bb,cc):
    print aa+bb+cc

dict2 = {'aa':8,'bb':7,'cc':11}

total(**dict2)

def fibs(n):
    """
    This is a Fibonacci sequence.
    """
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == "__main__":
    lst = fibs(10)
    print lst




   
