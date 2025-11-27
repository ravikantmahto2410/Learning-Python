# username = "Harrier"

#### how we use  scope in python

# def test():
#     pass

# if True:
#     pass

### In python , jitni baar bhi hum indentation dekhe na uska matlab hai humne ek indentation start kiya hai
#### In python jitni baar bhi hum ek function bana rahe that simply means ki hum ek ghar bana rahe hai memory space mein


###### Now lets start the learning

# username = "Tata Motors"
# def func():
#     # username = "Sierra"
#     print(username)

# print(username)
# func()


##### Next example 

# x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)



#####Example - 03:

# x = 99
# def func3():
#     x = 88

# print(x)



#####Example - 04:
#### Note ye example ke jaisa kaam nahi karna
# x = 99
# def func3():
#     global x
#     x = 12

# func3()
# print(x)


##### Example - 05
# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()

# f1()

### Example-06

# x = 99

# def f1():
#     #x = 88
#     def f2():
#         print(x)
#     f2()

# f1()


# #### Example- 07

# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# myResult = f1()
# myResult()  #### ye f2 ko execute kar raha hai



#### Example- 08

x = 99

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()  

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))