def ExamResult(m, p, c):
    return min(m, p, c) >= 45

for _ in range(10):
    m, p, c = map(int, input('Enter the marks of "maths", "physics" and "chemistry": ').split())
    print('Pass'  if ExamResult(m, p, c) else 'Fail')