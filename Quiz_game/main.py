from data import question_data
from question_model import Question
from quiz_brain import Quiz

questions = []

for que in question_data:
    questionss = que["text"]
    answerr = que["answer"]
    newqun = Question(questionss, answerr)
    questions.append(newqun)

quiz = Quiz(questions)
while quiz.sufficeintQns():
    quiz.nextQn()

print(f"Your Final score is {quiz.score}")
