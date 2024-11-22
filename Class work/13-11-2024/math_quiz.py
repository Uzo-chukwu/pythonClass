import random  

def math_quiz():
    score = 0
    failed_questions = []
    
    for count in range(10):
        number_one = random.randint(1, 1000)
        number_two = random.randint(1, 1000)  

        if count < 5:  
            answer = number_one + number_two
            user_answer = int(input(f"What is {number_one} + {number_two}? "))

            if user_answer == answer:
                score += 1
            else:
                failed_questions.append((f"{number_one} + {number_two}", answer, user_answer))

        elif count < 8:  
            answer = number_one * number_two  
            user_answer = int(input(f"What is {number_one} * {number_two}? "))

            if user_answer == answer:
                score += 1 
            else:
                failed_questions.append((f"{number_one} * {number_two}", answer, user_answer))

        else:  
            answer = number_one - number_two
            user_answer = int(input(f"What is {number_one} - {number_two}? "))

            if user_answer == answer:
                score += 1
            else:
                failed_questions.append((f"{number_one} - {number_two}", answer, user_answer))

    print(f"\nQuiz finished! Your score is {score} out of 10.")
    print(f"You failed {10 - score} questions.")
    
    if failed_questions:
        print("\nCorrections:")
        for question, correct_answer, user_answer in failed_questions:
            print(f"Question: {question}")
            print(f"Your Answer: {user_answer}")
            print(f"Correct Answer: {correct_answer}\n")

math_quiz()