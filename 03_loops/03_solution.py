# number = 3 #suppose we are printing the table of 3

# for i in range(1, 11):
#     print(number, 'x', i, '=', number * i ) # we will get the table 


#############  Now we write the actual solution of this problem

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i, '=', number * i)