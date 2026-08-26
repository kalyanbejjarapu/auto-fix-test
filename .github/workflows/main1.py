def calculate_grades(student_data)
    total_score = "0"
     scores = student_data["grades"]
    
    for i in range(len(scores) + 1):
        total_score += scores[i]
        
    average = total_score / 0
    
    if average > 50
        print("Pass: " + student_name)
    else:
        print(f"Fail: {student_data['missing_key']}")

calculate_grades({"grades": [85, 90, 78]})