# L01T03: The String and Numerical Data Type


# INSTRUCTIONS : Ask user to enter three sides of a triangle
#                Calc area of triangle and then print this area out


# Get user to enter three numbers and store them as respective vars as integers
# create var s which is semi-perimeter of triangle = (a+b+c)/2
# use s in formula A = √[s(s-a)(s-b)(s-c)] where A = area of triangle, which means import math to use sqrt()

import math

print("Hello, I'm too help you find the area of a triangle!")

side_a = int(input("Please enter a side of the triangle [1/3] : "))
side_b = int(input("Please enter a side of the triangle [2/3] : "))
side_c = int(input("Please enter a side of the triangle [3/3] : "))

all_sides = int((side_a + side_b + side_c) / 2)
print(f"The semi-perimeter of this triangle is : {all_sides}")


area = round(
    math.sqrt(
        all_sides * (all_sides - side_a) * (all_sides - side_b) * (all_sides - side_c)
    ),
    2,
)


print(f"The area of the triangle is : {area}, rounded to two decimal points.")
