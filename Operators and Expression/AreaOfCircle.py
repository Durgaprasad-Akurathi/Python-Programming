import math

def AreaofCircle(radius):
    Area = math.pi*radius*radius
    return Area


radius = int(input('Enter the radius of the circle: '))

print("Area of the Circle is: ", AreaofCircle(radius))