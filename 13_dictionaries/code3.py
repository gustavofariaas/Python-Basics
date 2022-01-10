student_attendence = {"Rolf": 94, "Bob": 80, "Anne": 100}

for student in student_attendence:
    print(f"{student}: {student_attendence[student]}")

for student, attendence in student_attendence.items():
    print(f"{student}: {attendence}")