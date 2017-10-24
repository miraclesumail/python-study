# coding=utf-8
import time
import random
from functools import wraps
import logging

a = [1,2,3,4]
b = [5,6,7,8]

c= [(x,y) for x in a for y in b]
print c

sa = filter(lambda x:x!='s','dsxsdfs')
print sa

# 这个是迭代器
ab = (str(x) for x in range(10))
print type(ab)
print next(ab)
print next(ab)

# 用classmethod修饰的也可以用实例调用
class who(object):
      def __init__(self,age):
          self.age = age

      def foo(self):
          pass    

      @classmethod
      def say(cls):
          print "executing class_foo(%s)"%(cls)

      @staticmethod
      def speak(ss):
          print ss    

# cls打印的事__main__.who staticmethod不必带cls或self 是一个普通函数
aa = who(8)
print aa.say()   
print who.say() 
print who.speak('wcd')
print aa.foo
print aa.say
print aa.speak

# 注意不一定要写self 写cls一样
class B:
    # Equivalent definition of a class method
    def method(cls):
        print 'say'
    method = classmethod(method)       

print B.method()    

def timethis(fn):
    '''
    decrorator that reports the excution time
    '''

    # 这里添加@wraps是防止重写函数名
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = fn(*args,**kwargs)
        end = time.time()
        print fn.__name__,end - start
        return result
    return wrapper

@timethis
def countdown(n,m):
    '''
    Counts down ff
    '''
    print m
    while n>0:
         n -= 1

countdown(100000,'sss')    
print countdown.__doc__
print countdown.__name__

# python3中才有
# origin = countdown.__wrapped__

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

# 注意打印的顺序 decrotar1最先
print add(3,4)

def cal(a,b):
    print a+b

# 带参数的装饰
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            abc = (random.randint(1,10),random.randint(1,10))
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(cal,abc)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1(fn,arg):
    fn(*arg)

myfunc1(cal,(2,3))    

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # 通过这里改变message level的值
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

# >>> import logging
# >>> logging.basicConfig(level=logging.DEBUG)
# >>> add(2, 3)
# DEBUG:__main__:add
# 5
# >>> # Change the log message
# >>> add.set_message('Add called')
# >>> add(2, 3)
# DEBUG:__main__:Add called
# 5
# >>> # Change the log level
# >>> add.set_level(logging.WARNING)
# >>> add(2, 3)
# WARNING:__main__:Add called
# 5
# >>>