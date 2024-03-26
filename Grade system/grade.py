def get_grade(score):
    grades = {
        (90, 100): 'A Excellent',
        (87, 90): "A-",
        (84, 87): "B+",
        (80, 84): 'B',
        (77, 80): "B-",
        (74, 77): "C+",
        (71, 74): "C",
        (68, 71): "C-",
        (65, 68): "D+",
        (63, 65): "D",
        (61, 63): "D-"
    }
    
    for cutoff, grade in sorted(grades.items(), reverse=True):
        if score >= cutoff[0]:
            return grade
    return 'F'

# Continuous execution
while True:
    try:
        score = int(input("Enter your score (or type 'exit' to quit): "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100")
            continue
        if score == 'exit':
            break
        grade = get_grade(score)
        print(f'Your grade is: {grade}')
    except ValueError:
        print("Invalid input! Please enter a valid score or type 'exit' to quit.")
