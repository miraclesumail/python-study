# coding=utf-8
import inspect
import random
class animal(object):
      gender = 'female'
      age = 18

      def dd(self):
          pass

for key,val in inspect.getmembers(animal):
    print key,'==',val          

print type(animal)    
print type(animal())

#<type 'type'>
#<class '__main__.animal'>

s1 = 'wcnm'
print dir(s1)
print dir(animal)
print getattr(animal(),'age')
print getattr(animal,'age')

print filter(lambda x: x.strip('__') == x ,dir(animal))

first = []
for i in range(3):  
    
    def foo(x,y=i): 
        print(x * y)  
       
    first.append(foo) 

for f in first:
    f(2)

# 注意这种es6里的解构
f1,f2,f3 = first    
print f3(9)

# 这里感觉很奇怪 dict就可以
n = 0
def outter():
   
    def inner():
        global n
        n += 1
        print n

    return inner

aa = outter()
aa()
aa()    
print n    

def test1():
    asd = {'count':1}
    
    def test2():
        asd['count'] += 1
        print asd['count']

    return test2

bb = test1()
bb()
bb()

def yield_test(n):
    for i in range(n):
        yield call(i)
        print 'i=',i

    print 'end'

def call(i):
    return i*3

aa = yield_test(3)
print next(aa)
print next(aa)
print next(aa)
print '-----'

# 可以理解为i = call(i) 可以通过next调用
for i in yield_test(5):
    print i,'---'    

def cf():
    while True:
        val = yield
        print val,

def pf(c):
    while True:
	val = random.randint(1,10)
	c.send(val)
	yield

if __name__ == '__main__':
    c = cf()
    c.send(None)
    p = pf(c)

    for wow in range(10):
        next(p)