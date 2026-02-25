def AreaOfTrapezium(a, b, height):
    Area = 1/2 * (a + b) * height
    return Area


a, b = map(int, input("Enter the lengths of the parallel sides: ").split())
height = int(input('Enter the perpendicular distance between the two parallel sides: '))

print("Area of the Trapezium is: ", AreaOfTrapezium(a, b, height))