from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain


question_bank = []

for i in range(len(question_data)):
   question_bank.append(Question(question_data[i]["text"] ,question_data[i]["answer"]))

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
   quiz.next_question()
