import random

def collect_student_data():
	students = []
	for i in range(10):
		student_name = input(f"Enter student {i+1} name: ")
		java_score = random.randint(1, 100)
		python_score = random.randint(1, 100)
		data_science_score = random.randint(1, 100)
		design_thinking_score = random.randint(1, 100)
    
	while not (1 <= java_score <= 100 and 
		1 <= python_score <= 100 and 
		1 <= data_science_score <= 100 and 
		1 <= design_thinking_score <= 100):
		print("Invalid score. Please enter scores between 1 and 100.")

        
           
        
	student = {
            "name": student_name,
            "java": java_score,
            "python": python_score,
            "data_science": data_science_score,
            "design_thinking": design_thinking_score
        }
	students.append(student)
	return students

def calculate_best_worst(students):
	best_worst = {}
	subjects = ["java", "python", "data_science", "design_thinking"]
    
	for subject in subjects:
		best_student = worst_student = students[0]["name"]
		best_score = worst_score = students[0][subject]
        
	for student in students:
		score = student[subject]
		if score > best_score:
			best_student = student["name"]
			best_score = score
		elif score < worst_score:
			worst_student = student["name"]
			worst_score = score
        
	best_worst[subject] = {
            "best": {"name": best_student, "score": best_score},
            "worst": {"name": worst_student, "score": worst_score}
        }
    
	return best_worst

def main():
    students = collect_student_data()
    best_worst = calculate_best_worst(students)
    
    print("Best and Worst Performing Students:")
    for subject, data in best_worst.items():
        print(f"\n{subject.capitalize().replace('_', ' ')}:")
        print(f"Best: {data['best']['name']} - {data['best']['score']}")
        print(f"Worst: {data['worst']['name']} - {data['worst']['score']}")

if __name__ == "__main__":
    main()


