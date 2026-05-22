import csv
import json
import random

def getData():
    data = []

    with open('softwareDev34/Unit3/AOS1/SAT/quiz.csv') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data


quizes = getData()

for quiz in quizes:
    if quiz[0] == "Quiz 2":
        quizToBeTaken = json.loads(quiz[1])

possibleAnswers = []
for possibleAnswer in quizToBeTaken.values():
        possibleAnswers.append(possibleAnswer)


for question, answer in quizToBeTaken.items():
    q1Ansswers = []

    incorrectAnswers = [ans for ans in possibleAnswers if ans != answer]
    q1Ansswers = random.sample(incorrectAnswers, 3)

    answerPos = random.randint(0, 3)
    q1Ansswers.insert(answerPos, answer)

    print(question)
    print("Possible answers:")

    for i, ans in enumerate(q1Ansswers):
        print(f"{i + 1}. {ans}")

    
    userAnswer = input("Answer: ")
    if userAnswer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)
    


