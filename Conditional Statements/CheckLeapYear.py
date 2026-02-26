def CheckLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return "Leap Year"
        else:
            return "Not a Leap Year"
        
    elif year % 4 == 0:
        return "Leap Year"
    
    else: return "Not a Leap Year"


print(CheckLeapYear(int(input("Enter the year: "))))