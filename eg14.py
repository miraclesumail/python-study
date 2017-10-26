# encoding=utf-8
import math
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    # 如果__str__  没有定义 就会使用__repr__
    def __str__(self):
        return '卧槽 ({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 5)
p
print p    

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

import operator
x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

#或者
sorted_x = sorted(x.items(), key=lambda x:x[0])
print sorted_x  
# [(0,0),(1,2),(2,1),(3,4)]
print(dict(sorted_x))  
{0:0,1:2,2:1,3:4}

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
    age = 18

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

    # __私有方法和属性
    def __change(self,age):
        self.age = age

    def abc(self,age):
        self.__change(age)    

counter = JustCounter()
counter.count()
counter.count()
print counter.age
counter.abc(99)
print (counter.publicCount)
print counter._JustCounter__secretCount 


def max(m,n):
    aa = 0
    b,c = m,n
    while  m%n > 0:
          aa = m%n
          m = n
          n = aa
    return (b*c)/aa

print(max(121,99))    

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


         
    






