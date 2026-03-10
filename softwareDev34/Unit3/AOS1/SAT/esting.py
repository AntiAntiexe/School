import csv
import json
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",

}

def getData():
    data = []

    with open('softwareDev34/Unit3/AOS1/SAT/quiz.csv') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

#print(getData())

quizes = getData()

for quiz in quizes:
    if quiz[0] == "Quiz 1":
        quizToBeTaken = json.loads(quiz[1])
#print(quizToBeTaken)
for question, answer in quizToBeTaken.items():
    userAnswer = input(question + " ")
    if userAnswer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)
    
    

