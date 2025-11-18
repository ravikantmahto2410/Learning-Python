import math

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = circle_stats(3);

print("Area = ", a, "Circumference = ", c)

#  HW : Since here the after decimal lots of digit are coming , our homework is what should we use so that whenever ans coming in lots of digits , we can reduce to digits to like one two or whatever we want , there should be some method in math