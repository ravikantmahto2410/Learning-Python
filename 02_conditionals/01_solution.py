# userage = 25;
#  we can also take input like  userage = input("Enter the user age : ")
# we can also convert the entered value into the user there itself like this age = int(input("Provide me an age : "))
#  we can also do like for more readability
#       age = input("Provide me an age : ")
#       age_in_int = int(age)

age = 25;
if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")
