items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()  ####set apne aap mein unique values rakhta hai, it does not take the duplicates value

for item in items:
    if item in unique_item: # this returns the true or false 
        print("Duplicates:", item)
        break
    
    unique_item.add(item) ###  this means if the item is not found on the set or bucket then add that item in the bucket
    