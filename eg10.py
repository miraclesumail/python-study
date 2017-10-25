# coding=utf-8
import types
from collections import namedtuple
# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price
def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
    'ww':5    # 这里面也可以写属性
}


Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
s = Stock('ACME', 50, 91.1)

word = namedtuple('word',['x','y','z'])
ww = word(3,4,5)
print len(ww)
print ww[0]

class test(object):
    # new会覆盖 __init__
    def __new__(cls, *args):
        print args

    def __init__(self,name,age):
        print 'axiba'    

tt = test('ww',12)     

import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        print (cls)
        super().__init__(*args, **kwargs)
        
        for n, name in enumerate(cls._fields):
            print (str(property(operator.itemgetter(n)))) 
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        print ('sss')
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)
    
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

s = Stock('ACME', 50, 91.1)
print (s.name)   
print s
# ('ACME', 50, 91.1)

# 注意元类的init永远在 new之前
