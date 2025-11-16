# def square_of_num(number):
#     print(number ** 2)

# ####Function ho gya hai tyaar

# square_of_num(6)

## now a bit better 
# def square_of_num(number):
#     print(number ** 2)

# result = square_of_num(4)
# print(result)  ###here we get none means empty because


# variation 3
# def square_of_num(number):
#     return number ** 2

# result = square_of_num(4)
# print(result)  #### this will return 16

# Variation 4
def square_of_num(number):
    return number ** 2

result = square_of_num(4)
print(square_of_num(4))  #### this will return 16 , but this 16 is not returned due to variable result, its because first the square_of_num(4) is evaluated and this returns 16 and then it is printed
