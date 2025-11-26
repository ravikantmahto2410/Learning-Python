# def print_kwargs(name, power):
#     print("Name: ", name, " Power : ",power)


# print_kwargs(name = "Shaktiman", power="laser")


#####Investigative starts

# def print_kwargs(name, power):
#     print("Name: ", name, " Power : ",power)

# print_kwargs( power="laser", name = "Shaktiman") ####Still we are getting the result in the same order that means we can flips the order, agar humein koi user named arguments de raha hai to #### ye bhi ek tarika hai function ke definitions ko call karane ka


#######But we want something like this




def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    

print_kwargs( name = "Shaktiman", power="laser")
print_kwargs( name = "Shaktiman")
print_kwargs( name = "Shaktiman", power="laser", enemy = "Dr.Jackal")













