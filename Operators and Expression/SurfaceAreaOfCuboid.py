def SurfaceAreaOfCuboid(length, breadth, height):
    TotalSurfaceArea = 2 * (length * breadth + length * height + breadth * height)
    return TotalSurfaceArea


length = int(input('Enter the Length of the Cuboid: '))
breadth = int(input('Enter the breadth of the Cuboid: '))
height = int(input('Enter the base of the Cuboid: '))

# length, breadth, height = map(int, input('Enter the length, breadth and height: ').split())

print("Area of the Triangle is: ", SurfaceAreaOfCuboid(length, breadth, height))