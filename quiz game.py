import time
import random

# Quiz Questions
quiz_data = {
    "Science": [
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": "Carbon Dioxide"
        }
    ],
    "History": [
        {
            "question": "Who was the first President of the United States?",
            "options": ["Abraham Lincoln", "George Washington", "John Adams", "Thomas Jefferson"],
            "answer": "George Washington"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1940", "1945", "1939", "1950"],
            "answer": "1945"
        }
    ]
}

# Game settings
use_timer = True
timer_seconds = 10

def ask_question(question_data, question_num):
    print(f"\nQuestion {question_num}: {question_data['question']}")
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    
    if use_timer:
        print(f"You have {timer_seconds} seconds to answer...")

    start_time = time.time()
    while True:
        try:
            if use_timer and (time.time() - start_time) > timer_seconds:
                print("⏰ Time's up!")
                return False
            answer = input("Your choice (1-4): ")
            if answer.isdigit() and 1 <= int(answer) <= 4:
                selected_option = question_data["options"][int(answer)-1]
                return selected_option == question_data["answer"]
            else:
                print("Please enter a valid option (1-4).")
        except Exception as e:
            print("Error:", e)

def start_quiz():
    print("🎮 Welcome to the Quiz Game!")
    name = input("Enter your name: ")
    print(f"\nHi {name}! Choose a category:")

    categories = list(quiz_data.keys())
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
    cat_choice = int(input("Select category number: "))
    selected_category = categories[cat_choice - 1]

    questions = quiz_data[selected_category]
    random.shuffle(questions)

    score = 0
    for i, question in enumerate(questions, 1):
        if ask_question(question, i):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {question['answer']}\n")

    print(f"🏁 Quiz Completed! Your score: {score}/{len(questions)}")
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    start_quiz()
