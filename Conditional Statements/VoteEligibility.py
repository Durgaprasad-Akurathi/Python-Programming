def VoteEligibility(age):
    return age >= 18

age = int(input("Enter the age of the voter: "))
print('Eligible' if VoteEligibility(age) else 'Not Eligible')