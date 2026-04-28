#student profile card
student = {"full_name":"Enziwe Dlamini", "city":"Cape Town", "age":20, "courses":["Information systems", "FCC", "Code academy"], "gpa":87.32, "is_graduated":False}

print("=========================")
print("Student Profile Card")
print("=========================")
print(f"Name:   {student['full_name'].upper()}")
print(f"Age:   {student['age']}")
print(f"City:   {student['city']}")
print(f"GPA:   {student['gpa']}")
print(f"Graduated:   {student['is_graduated']}")
print(f"Courses:   {' | '.join(student['courses'])}")
print("=========================")
print(f"Profile created for: {student['full_name']}")