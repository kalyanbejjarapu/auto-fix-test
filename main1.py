def calculate_grades(student_data):
    # Syntax & runtime errors for AI Auto-Fix testing
    total_score = 0
    scores = student_data["grades"]
    
    # Auto-fixed boundary index
    for i in range(len(scores)):
        total_score += scores[i]
        
    average = total_score / len(scores)
    
    if average > 50:
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    student_name = student_data.get("name", "Student")
    print("Pass: " + student_name)
    else:
        print(f"Fail: {student_data['missing_key']}")

calculate_grades({"grades": [85, 90, 78]})