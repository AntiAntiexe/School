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

quizToBeTaken = None
for quiz in quizes:
    if quiz[0] == "Quiz 2" and quiz[1].startswith("Anton"):
        quizToBeTaken = json.loads(quiz[2])
        break

if quizToBeTaken is None:
    raise ValueError("Quiz 2 for Anton was not found.")


def playQuiz(quizToBeTaken):
    print("Starting quiz...")
    print(quizToBeTaken)

    for question, answer in quizToBeTaken.items():
        possibleAnswers = list(quizToBeTaken.values())
        incorrectAnswers = [ans for ans in possibleAnswers if ans != answer]
        options = random.sample(incorrectAnswers, 3)

        answerPos = random.randint(0, 3)
        options.insert(answerPos, answer)

        print(question)
        print("Possible answers:")

        for i, ans in enumerate(options):
            print(f"{i + 1}. {ans}")

        userChoice = input("Answer (1-4): ")
        try:
            selectedAnswer = options[int(userChoice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number from 1 to 4.")
            continue

        if selectedAnswer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", answer)

def showQuizzes(username):
    print("Available quizzes:")
    for quiz in quizes:
        if quiz[1].startswith(username):
            print(quiz[0])
    
#playQuiz(quizToBeTaken)

showQuizzes("Jay")




