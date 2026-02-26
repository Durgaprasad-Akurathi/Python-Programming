'''
#1
def MonthName(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    if 0 <= month <= 12:
        return months[month-1]
    else:
        return 'Invalid Month'

print(MonthName(int(input('Enter the Month Number: '))))

#2
def MonthName(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    try:
        if month < 1:
            raise IndexError
        return months[month - 1]
    except IndexError:
        return 'Invalid Month'

print(MonthName(int(input('Enter the Month Number: '))))

'''
    
#3
def MonthName(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'
    else:
        return 'Invalid Month'

print(MonthName(int(input('Enter the Month Number (1-12): '))))


#4
'''
def MonthName(month):
    months = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    return months.get(month, 'Invalid Month')

print(MonthName(int(input('Enter the Month Number (1-12): '))))
'''
