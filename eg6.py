# coding=utf-8

class noInstance(type):
      def __init__(self, *args, **kwargs):
        print 'axiba'

      def __call__(self, *args, **kwargs):
        print self
        print args
        print kwargs
        
       
class Spam():
      __metaclass__ = noInstance
 
      def __init__(self,age,gender):
          self.age = age
          self.gender = gender

      @staticmethod
      def say(ss):
          print ss

s = Spam(18,'dd',year = 2012,month = 8)       
sd = Spam(18,'dd',year = 2012,month = 8) 
 

class Singleton(type):

    # 注意init只调用一次  在这里先设定__instance__
    def __init__(self, *args, **kwargs):
        self.__instance = None
        print 'first'

    def __call__(self, *args, **kwargs):
        print 'wcnmb'
        if self.__instance is None:
            self.__instance = 'sssss'
            return self.__instance
        else:
            return self.__instance

class test():
    __metaclass__ = Singleton
    def __init__(self):
        print('Creating Spam')

a = test()

b = test()
print (a is b)

c = test()
print (a is c)


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# # Example
# class Spam(metaclass=Cached):
#     def __init__(self, name):
#         print('Creating Spam({!r})'.format(name))
#         self.name = name


# >>> a = Spam('Guido')
# Creating Spam('Guido')
# >>> b = Spam('Diana')
# Creating Spam('Diana')
# >>> c = Spam('Guido') # Cached
# >>> a is b
# False
# >>> a is c # Cached value returned
# True
# >>>      
                 