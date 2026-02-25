''' Method-1

length = int(input('Enter the Length of the Rectangle: '))
breadth = int(input('Enter the breadth of the Rectangle: '))

Area = length * breadth

print("Area of the rectangle is: ", Area)

'''


''' Method-2'''
def AreaOfRectangle(length, breadth):

    Area = length * breadth
    return Area

length = int(input('Enter the Length of the Rectangle: '))
breadth = int(input('Enter the breadth of the Rectangle: '))

print("Area of the rectangle is: ", AreaOfRectangle(length, breadth))
