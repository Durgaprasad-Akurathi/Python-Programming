'''
#1
def WeekDayName(day):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    if 0 <= day < 7:
        return days[day]
    else:
        return 'Invalid day'

print(WeekDayName(int(input('Enter the Day Number: '))))

#2
def WeekDayName(day):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    try:
        return days[day]
    except IndexError:
        return 'Invalid day'

print(WeekDayName(int(input('Enter the Day Number: '))))

'''

'''
#3
def WeekDayName(day):
    days = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    
    return days.get(day, 'Invalid day')

print(WeekDayName(int(input('Enter the Day Number: '))))

'''

#4
def WeekDayName(day):
    if day>=0 and day<7:
        if day == 0:
            return 'Sunday'
        elif day == 1:
            return 'Monday'
        elif day == 2:
            return 'Tuesday'
        elif day == 3:
            return 'Wednesday'
        elif day == 4:
            return 'Thursday'
        elif day == 5:
            return 'Friday'
        elif day == 6:
            return 'Saturday'
        
    else: return 'Invalid day'

print(WeekDayName(int(input('Enter the Day Number: '))))
        