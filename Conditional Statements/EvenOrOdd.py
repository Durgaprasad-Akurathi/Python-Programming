def EvenOrOdd(n):
    return n%2 == 0

n = int(input('Enter the number: '))
print('Even' if EvenOrOdd(n) else 'Odd')