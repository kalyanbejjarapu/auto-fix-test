def calculate_average(numbers):
    # Bug: 'totl' is referenced before assignment (UnboundLocalError)
    totl = 0
    for n in numbers:
        totl += n
    return totl / len(numbers)

# Test list
scores = [85, 90, 78, 92]
print("Average score is:", calculate_average(scores))
