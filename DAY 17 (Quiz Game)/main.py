from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
