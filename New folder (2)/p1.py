import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Elapsed time ={end-start} second")
        return result
    return wrapper
@timer
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
fact(100)
