# coding=utf-8
import string

list1 = [1,2,3]
list2 = [3,4,5]
aa = zip(list1,list2)
print aa

print sum((x*y for x,y in aa))

def reduce(function, iterable, initializer=2):
    
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:    
            raise TypeError('reduce() of empty sequence with no initial value')    
    accum_value = initializer                                                                   
    for x in iterable:
        accum_value = function(accum_value, x)    
    return accum_value

print reduce(lambda x,y:x+y,[1,2,3])

print reduce(lambda x,(a,b): x + a*b , aa ,3)

a = 'dfg ff '
b = a.strip()
c = a.strip('d')
print b
print c

table = string.maketrans('ho','at')
cc = 'hosssho jj hosss'
dd = cc.translate(table,' ')
print dd

count = 'sdadadaffa'.count('a',1,5)
print count

# 注意此时是float  如果是int 用atoi

num1 = '2345.33'
num2 = string.atof(num1)
print num2

str1 = 'wcbnfdkke'
print str1.endswith('n',1,3)

class person(object):
      isAdult = True
      age = 18

      def __len__(self):
          return self.age

class boy(person):
      isGirl = False

      def __init__(self,age):
          self.age = age

      def total(self):
          pass            

pp = person()
qq = boy(22)
print person.__dict__
print boy.__dict__
print qq.__dict__
print len(pp)

# 可以通过__dict__修改age
qq.__dict__['age'] = 23
print qq.age

# 通过property返回一个属性
class chicken(object):
      gg = 'fuck'
      def __init__(self,age):
          self.age = age

      def getAdult(self):
          adult = True if self.age > 18 else False
          return adult

      adult = property(getAdult)

# 所有的实例共享 gg属性
cc1 = chicken(11)
cc2 = chicken(22)
print cc1.gg,cc2.gg      

print cc1.adult
print cc2.adult

cc2.age = 17
print cc2.adult

class number(object):
    def __init__(self, value):        
        self.value = value  
        print '<--init'  
    def getNeg(self):  
        print '<--getNeg'  
        return self.value * -1  
    def setNeg(self, value):  
        print '<--setNeg'  
        self.value = (-1) * value  
    def delNeg(self):  
        print("value also deleted")  
        del self.value  
    neg = property(getNeg, setNeg, delNeg, "I'm negative")  

nm = number(23)
print nm.neg 
nm.neg = 88
print nm.value

del nm.neg
print nm.value   

# __getattr__只能用来查询不在__dict__系统中的属性
class bird(object):  
    feather = True  
  
class chicken(bird):  
    fly = False  
    def __init__(self, age):  
        self.age = age  
    def __getattr__(self, name):  
        if name == 'adult':  
            if self.age > 1.0:   
                return True  
            else:   
                return False  
        else:   
            raise AttributeError(name)  
  
summer = chicken(2)  
  
print(summer.adult)  
summer.age = 0.5  
print(summer.adult)  
  
print(summer.male)  


