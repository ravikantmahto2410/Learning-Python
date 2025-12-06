# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result =  func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
    
#     return wrapper


# def example_function(n):
#     time.sleep(n)

# example_function(2)



# ############## Now to make toll
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)  #### Now jaise hi hum isko call karenge to ye timer function se hi hoke gujrega

