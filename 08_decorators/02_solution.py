

# def greet(name, greeting = "Hello"):
#     print(f"{greeting}, {name}")

# greet("chai", greeting="Hanji Chai Ho jaaye")

########################## abhi tak ho gya ek basic function , now we will make the tollBoooth

# def debug(func):
#     def wrapper(*args, **kwargs):
#         return func(*args,**kwargs)
#     return wrapper

# def greet(name, greeting = "Hello"):
#     print(f"{greeting}, {name}")

# greet("chai", greeting="Hanji Chai Ho jaaye")


##### ye hai basic decorator
# def debug(func):
#     def wrapper(*args, **kwargs):
#         return func(*args,**kwargs)
#     return wrapper

# def greet(name, greeting = "Hello"):
#     print(f"{greeting}, {name}")


##### just  upar wala  bbhi hai ek  decorator
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs{kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")
@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="Hanji Chai Ho jaaye")

###### just ye upar wala bhi hai bar minimum decorator

