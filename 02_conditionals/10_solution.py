species = "Dog"
age = 1

if species == "Dog":
    if age < 2:
        food = "Puppy Food"
    else :
        food = "Chicken"
elif species == "Cat":
    if age > 5:
        food = "Senior cat food"
    else :
        food = "Puppy cat food"

print("The food of the species is", food)