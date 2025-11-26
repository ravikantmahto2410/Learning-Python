# def even_generator(limit):
#     for i in range(2,limit + 1, 2):
#         return i

# print(even_generator(10))
# ####Niss upar wale function ko ab usage kon le rha wo depend karta hai


# #####Now we are doing something using list
# def even_generator(limit):
#     li = []
#     for i in range(2,limit + 1, 2):
#         li.append(i)
#     return li



# print(even_generator(10)) ### This is giving probem that this is returning a list , that we didn't wanted

######## Now lets take to the next method , some people also do like this but this gives more probelem
# def even_generator(limit):
#     for i in range(2,limit + 1, 2):
#         return i
    
# for num in even_generator(10):
#     print(num)


######## now lets see how we can do yield in python

def even_generator(limit):
    for i in range(2,limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)
    


