
def gradeCheck(grade):
    if grade >= 90:
        return 'A'
    elif 80 <= grade <=89:
        return 'B'    
    elif 60 <= grade <=79:
        return 'C'   
    elif 40 <= grade <=59:
        return 'D'
    else:
        return 'F'
    

while True:
    grade = int(input('Enter your grade: '))
    print(f'{gradeCheck(grade)}')
