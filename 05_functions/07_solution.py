# def sum_all(*args): ### Note here we can  write any thing in place of args , but we have to must write the *. if we want that this function can accept any number of parameters
#                          #### here * tells that there is possibility of multiple parameters that will be coming
#     sum(args)  ### Note : sum python ka default  method hota hai jo ki iske ander ki saari values ko sum kar deta hai


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))



# ##### Now lets do how its working
# def sum_all(*args): ### Note here we can  write any thing in place of args , but we have to must write the *. if we want that this function can accept any number of parameters
#                          #### here * tells that there is possibility of multiple parameters that will be coming
#     print(*args)
#     sum(args)  ### Note : sum python ka default  method hota hai jo ki iske ander ki saari values ko sum kar deta hai


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4))



#### Now lets see how these lines are working
# def sum_all(*args): ### Note here we can  write any thing in place of args , but we have to must write the *. if we want that this function can accept any number of parameters
#                          #### here * tells that there is possibility of multiple parameters that will be coming
#     print(args)
#     sum(args)  ### Note : sum python ka default  method hota hai jo ki iske ander ki saari values ko sum kar deta hai


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))

# ##the the function that we just write down down gives tuples , jo ki apne aap mein iterateable



# ######Now since the tuples is iteretable can we iterate and do some operation like multiplication division and all
# def sum_all(*args): ### Note here we can  write any thing in place of args , but we have to must write the *. if we want that this function can accept any number of parameters
#                          #### here * tells that there is possibility of multiple parameters that will be coming
#     print(args)
#     for i in args:
#         print(i*2)
#     sum(args)  ### Note : sum python ka default  method hota hai jo ki iske ander ki saari values ko sum kar deta hai


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))




#### now lets simplify it more
######Now since the tuples is iteretable can we iterate and do some operation like multiplication division and all
def sum_all(*args): ### Note here we can  write any thing in place of args , but we have to must write the *. if we want that this function can accept any number of parameters
                         #### here * tells that there is possibility of multiple parameters that will be coming
    print(args)
    for i in args:
        print(i*2)
    return sum(args)  ### Note : sum python ka default  method hota hai jo ki iske ander ki saari values ko sum kar deta hai


print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))




