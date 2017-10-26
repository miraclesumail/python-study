import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


class timethis:
    def __init__(self, label):
        self.label = label

    # yield之前
    def __enter__(self):
        self.start = time.time()

    # yield之后
    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))

with timethis('axiba'):
     n = 1000000
     while n > 0:
        n -= 1   

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
        
items = [1, 2, 3]
# 这个qwe就是 yield过来的working
with list_transaction(items) as qwe:
   qwe.append(4)
   qwe.append(5) 

with list_transaction(items) as working:
    working.append(6)
    working.append(7)
    # 如果在此处跑出一个错误 都不会执行
    
print(items)       

[1,2,3,4,5,6,7]  
