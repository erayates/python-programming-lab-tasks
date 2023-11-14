# Task 1
student_point = int(input("Enter the exam score: "))
while student_point < 50:
    if student_point < 0:
        print("You entered wrong score. Score should be between 0 and 100.")
    student_point = int(input("You failed. Enter the exam score again: "))
else:
    if student_point > 100:
        print('You entered wrong score. Score should be between 0 and 100.')
        student_point = int(input("Enter the exam score again: "))
    print('You passed the exam.')