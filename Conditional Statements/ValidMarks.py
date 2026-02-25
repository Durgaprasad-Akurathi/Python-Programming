def ValidMarks(Marks):
    return Marks >=0 and Marks <= 100

Marks = int(input('Enter the Marks: '))
print('Valid' if ValidMarks(Marks) else 'Not Valid')