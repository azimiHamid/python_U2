from utils_17.data import question_data
from utils_17.question_model import Question
from utils_17.quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    new_q = Question(q['text'], q['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")