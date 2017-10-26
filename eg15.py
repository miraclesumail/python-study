# coding=utf-8

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value) 

class asd:
     age = 18
     gender = 'male'        
       
     
pp = Proxy(asd())
pp._name = 'wwww'
print(pp._name)

class A:
     def __init__(self,age):
         self.age = age

class B(A):
     def __init__(self,age,name):
         super().__init__(age)
         self.name= name   

print(B(13,'www').__dict__)   

# 这2中写法都是一样的效果
class A:
     def __init__(self,age):
         self.age = age

class B(A):
     def __init__(self,age,name):
         A.__init__(self,age)
         self.name= name   

print(B(13,'www').__dict__)    

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')      

C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class '__main__.Base'>, <class 'object'>)

class Base:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender


class Sub(Base):
    pass

#  从这里看得出直接继承了base构造函数
sub = Sub(11,'male')
print sub.__dict__    

class Person:
    def __init__(self, name):
        print('fffff')
        self.name = name

    # Getter function
    @property
    def name(self):
        print('fter')
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")
        
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

# 

s = SubPerson('Guido')
s.name        

      