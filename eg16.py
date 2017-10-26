# coding = utf-8

class Integer:
    def __init__(self,name):
        self.name = name

    def __get__(self,instance,cls):
        print cls
        if isinstance is None:
            return self
        else:
            return instance.__dic__[self.name]

    def __set__(self,instance,value):
        print instance
        print value
        if not isinstance(value,int):
            raise TypeError('expected an int')
        instance.__dic__[self.name] = value 

    def __delete__(self,instance):
        del instance.__dic__[self.name]

class Point:
     x = Integer('x')
     y = Integer('y')

     def __init__(self,x,y):
         self.x = x
         self.y = y

pp = Point(3,4)
pp.x

def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate

class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price   



aa = set('acbasdc')
print(aa)
aa.update('xyzz')
print(aa)

bb = set(['y', 'python', 'b', 'o'])
print(bb)
bb.remove('python')
print(bb)

cc = set('abc')
dd = set('bcef')
ee = cc&dd
ff = cc|dd
print(type(ee))
print(ee)
print(ff)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

{'d', 'c', 'a', 'b', 's'}
{'d', 'c', 'x', 'z', 'a', 'y', 'b', 's'}
{'python', 'b', 'y', 'o'}
{'b', 'y', 'o'}
<class 'set'>
{'b', 'c'}
{'a', 'c', 'f', 'e', 'b'}             


class lazyproperty:
    def __init__(self, func):
        print(func)
        self.func = func

    def __get__(self, instance, cls):
        print(self.func)
        if instance is None:
            return self
        else:
            value = self.func(instance)
            aa = self.func.__name__ + 'ss'
            setattr(instance, aa, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius        
    
c = Circle(4.0)


print(c.area)
print(c.__dict__)

<function Circle.area at 0x1813f99c80>
<function Circle.perimeter at 0x1813f99ae8>
<function Circle.area at 0x1813f99c80>
Computing area
50.26548245743669
{'radius': 4.0, 'areass': 50.26548245743669}



