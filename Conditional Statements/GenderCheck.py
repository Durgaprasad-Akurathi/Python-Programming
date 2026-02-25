'''
def gender_check(gender):
    gender = gender.lower()
    return "Male" if gender == 'm' else "Female" if gender == 'f' else "Invalid Input"

print(gender_check(input("Enter the gender (M/F): ")))
'''

def GenderCheck(gender):
    gender = gender.lower()
    if gender == 'm':
        return 'Male'
    elif gender == 'f':
        return 'Female'
    else:
        return 'Invalid Input'

print(GenderCheck(input('Enter the gender (M/F): ')))
