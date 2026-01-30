import random

def run_quiz(questions):
    score = 0
    total = len(questions)

    print("Welcome to the Capitals MCQ Quiz!")
    print("Choose the correct option:\n")

    random.shuffle(questions)

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}: {q['question']}")
        options = q['options']
        random.shuffle(options)

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Your choice (1-4): "))
            if options[choice - 1].lower() == q['answer'].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1-4.")

        print(f"Current Score: {score}/{idx}\n")

    percentage = int((score / total) * 100)
    print("Quiz Completed!")
    print(f"You got {score} out of {total} questions right.")
    print(f"Your percentage: {percentage}%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 70:
        print("Great job! You have strong knowledge.")
    elif percentage >= 40:
        print("Not bad, but you can improve.")
    else:
        print("Keep practicing, you'll get better!")

if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "answer": "Paris",
            "options": ["Paris", "London", "Berlin", "Madrid"]
        },
        {
            "question": "What is the capital of Germany?",
            "answer": "Berlin",
            "options": ["Vienna", "Berlin", "Rome", "Lisbon"]
        },
        {
            "question": "What is the capital of Italy?",
            "answer": "Rome",
            "options": ["Madrid", "Rome", "Paris", "Bern"]
        },
        {
            "question": "What is the capital of Spain?",
            "answer": "Madrid",
            "options": ["Lisbon", "Madrid", "Berlin", "Vienna"]
        },
        {
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon",
            "options": ["Lisbon", "Bern", "Paris", "Rome"]
        },
        {
            "question": "What is the capital of Switzerland?",
            "answer": "Bern",
            "options": ["Vienna", "Berlin", "Bern", "Madrid"]
        },
        {
            "question": "What is the capital of Austria?",
            "answer": "Vienna",
            "options": ["Rome", "Vienna", "Paris", "Lisbon"]
        },
    ]

    run_quiz(quiz_questions)