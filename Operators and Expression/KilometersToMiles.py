def KilometersToMiles(kilometers):
    miles = kilometers * 0.621371
    return miles


kilometers = int(input('Enter the kilometers: '))

print("Miles for the given Kilometers is: ", KilometersToMiles(kilometers))