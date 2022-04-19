# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print('Enter the lengths of three side of a triangle:')
side1 = input('Side 1:')
side2  = input('Side 2:')
side3 = input('Side 3:')

if side1 != side2 and side2 != side3:
    print(f'A triangle with sides of {side1}, {side2} & {side3} is a Scalene triangle')

elif side1 == side2 and side2 == side3:
    print(f'A triangle with sides of {side1}, {side2} & {side3} is a Equallateral triangle')

elif side1 == side2 or side1 == side3 or side2 == side3:
    print(f'A triangle with sides of {side1}, {side2} & {side3} is a Isosceles triangle')