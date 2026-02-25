def WorkEligibility(age):
    return age >=18 and age <=60

age = int(input('Enter the age: '))
print('Eligible' if WorkEligibility(age) else 'Not Eligible')