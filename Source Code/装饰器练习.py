import time, functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):

        t1 = time.time()   
 
        result = func(*args, **kw)   
        t2 = time.time()   
        print('%s executed in %s ms' % (func.__name__, t2 - t1))    
        return result   
        
    return wrapper
@log
def s():
    s=1
    for i in list(range(50)):
      s=s+i
    print(s)
    return s
f=s
f()