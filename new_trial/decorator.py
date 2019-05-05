import time
import datetime
import pytz

# print(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))

start_time = time.time()

def decorator_func(original_func):
    def wrapper_func(*args,**kwargs):
        print("I want to print this func before {}".format(original_func.__name__))
        return original_func(*args,**kwargs)
    return wrapper_func



class decorator_class(object):
    def __init__(self,original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("I wanna print this class before".format(self.original_func.__name__))
        return self.original_func(*args,**kwargs)



# @decorator_func
@decorator_class
def display():
    print("this is the original function")




# @decorator_func
@decorator_class
def amaran():
    print("idhudhan da amaran")




# @decorator_func
@decorator_class
def displayInfo(name,age=10):
    print("display info ran with arguments {} and {}".format(name,age))



display()
# amaran()
displayInfo("deff",15)

end_time = time.time()-start_time

print(str(end_time)+" seconds")

