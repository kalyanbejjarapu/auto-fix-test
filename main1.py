def calculate_grades(student_data):
    # Syntax & runtime errors for AI Auto-Fix testing
    total_score = 0
    scores = student_data["grades"]
    
    for i in range(len(scores) + 1):  # IndexError: list index out of range
        total_score += scores[i]
        
    average = total_score / len(scores)
    
    if average > 50:
        print("Pass: " + student_name)  # NameError: student_name is not defined
    else:
        print(f"Fail: {student_data['missing_key']}")

calculate_grades({"grades": [85, 90, 78]})
