# coding=utf-8

class MixinA:
    def __getattr__(self, item):
       # Process item and return value if known
       if item == 'a':
           return 'MixinA'
       return super().__getattr__(item)

class MixinB:
    def __getattr__(self, item):
       # Process item and return value if known
       if item == 'b':
           return 'MixinB'

       return super().__getattr__(item)

class Example(MixinA, MixinB):
    # main class
    def __getattr__(self, item):
        if item == 'c':
           return 'MixinC'
        return super().__getattr__(item)

# e.c从自身拿不到 就会去找上级
e = Example()
print e.a    
print e.c

class MixinA:
    @property
    def a(self):
        return "MixinA"

class MixinB:
    @property
    def b(self):
        return "MixinB"

class Example(MixinA, MixinB):
    @property
    def c(self):
        return "MixinC"

e = Example()

print(e.a)
print(e.b)
print(e.c)

print hasattr(Example,'foo')
# 可以为类增加属性
Example.foo = 'foo'
print hasattr(Example,'foo')

print e.foo

ObjectCreatorMirror = Example # 你可以将类赋值给一个变量
print ObjectCreatorMirror()

print isinstance(e,Example)
print type(Example)
# <type 'classobj'>
print type(e)
# <type 'instance'>

def chooseClass(name):
    if name == 'foo':
       class foo(object):
           pass
       return foo
    else:
       class Bar(object):
            pass
       return Bar     

print chooseClass('foo')()    

# 如何使用type自定义类
Foo = type('Foo',(),{'age':18,'adult':True})

print Foo().age,Foo().adult

# Bar继承于Foo
Bar = type('Bar',(Foo,),{})
print Bar().age

# type就是Python的内建元类
age = 35
gender = 'male'
print age.__class__
print gender.__class__
print age.__class__.__class__
print gender.__class__.__class__

# tuple转化为 dict
lists = (('name','dddd'),('ddd','deee'))
dicts = dict((key.upper(),val) for key,val in lists)
print dicts

def upper_attr(future_class_name,future_class_parents,future_class_attr):
    print future_class_attr
    # {'bar': 'tip', '__module__': '__main__', '__metaclass__': <function upper_attr at 0x1022dbc08>}
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    dicts = dict((key.upper(),val) for key,val in attrs)
    return type(future_class_name, future_class_parents, dicts)

class qwe(object):
    __metaclass__ = upper_attr
    bar = 'tip'  

print hasattr(qwe,'BAR')    
print hasattr(qwe(),'BAR') 

class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        print 'aaa'
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)

class asd(object):
    __metaclass__ = UpperAttrMetaClass
    axiba = 'ssss'

    def __init__(self):
        print 'bbb'

aaa = asd()
print hasattr(aaa,'AXIBA')        





